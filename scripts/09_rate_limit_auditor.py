#!/usr/env/python3
"""
Script 09: Rate Limit Auditor
Probes target endpoints to observe sliding window thresholds and 429 triggers.
"""

import sys
import time
import urllib.request
import urllib.error

def audit_rate_limits(url: str, requests_count: int = 5):
    print(f"[*] Auditing rate limits for {url} ({requests_count} quick requests)...")
    
    for i in range(1, requests_count + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "TrespassingBot-Audit/1.0"})
            with urllib.request.urlopen(req, timeout=3) as response:
                print(f"[{i}] Status: {response.status}")
        except urllib.error.HTTPError as e:
            print(f"[{i}] HTTP Error Triggered: {e.code} (Possible rate limit or block)")
        except Exception as e:
            print(f"[{i}] Connection failed: {e}")
        time.sleep(0.2)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8080/"
    audit_rate_limits(target)
