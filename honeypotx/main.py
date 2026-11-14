"""
HoneypotX Gateway Main Application
Captures automated probes, inspects headers, and records interaction telemetry.
"""

from fastapi import FastAPI, Request
import logging
import json
from datetime import datetime

app = FastAPI(title="TrespassingBot Honeypot Gateway", version="1.0.0")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "HEAD"])
async def catch_all_trap(request: Request, full_path: str):
    client_ip = request.client.host
    method = request.method
    headers = dict(request.headers)
    query_params = dict(request.query_params)
    
    try:
        body = await request.json()
    except Exception:
        body = (await request.body()).decode("utf-8", errors="ignore")

    interaction_log = {
        "timestamp": datetime.utcnow().isoformat(),
        "client_ip": client_ip,
        "method": method,
        "path": f"/{full_path}",
        "headers": headers,
        "query_params": query_params,
        "body_preview": str(body)[:500]
    }

    # Log structured trap event
    logging.warning(f"[TRAP TRIGGERED] -> {json.dumps(interaction_log)}")

    # Return a realistic decoy response to keep automation engaged
    return {
        "status": "error",
        "code": 403,
        "message": "Access denied. Request flagged by edge security policy.",
        "incident_id": "err-sec-994821"
  }
  
