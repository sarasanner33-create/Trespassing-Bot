#!/usr/env/python3
"""
Script 08: Telemetry Streamer
Packages sandbox logs and honeypot events into standardized JSON streams.
"""

import json
from datetime import datetime

def format_telemetry(event_type: str, data: dict):
    payload = {
        "timestamp": datetime.utcnow().isoformat(),
        "source": "TrespassingBot",
        "event_type": event_type,
        "payload": data
    }
    return json.dumps(payload, indent=2)

if __name__ == "__main__":
    sample_data = {"status": "isolated_execution", "exit_code": 0}
    print(format_telemetry("sandbox_event", sample_data))
  
