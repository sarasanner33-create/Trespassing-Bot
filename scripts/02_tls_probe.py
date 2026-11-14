#!/usr/env/python3
"""
Script 02: TLS Handshake & Cipher Prober
Analyzes connection parameters and TLS configuration for target endpoints.
"""

import ssl
import socket
import sys
import json

def probe_tls(hostname: str, port: int = 443):
    print(f"[*] Probing TLS configuration for {hostname}:{port}...")
    context = ssl.create_default_context()
    
    try:
        with socket.create_connection((hostname, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                cipher = ssock.cipher()
                version = ssock.version()
                
                result = {
                    "hostname": hostname,
                    "tls_version": version,
                    "cipher_suite": cipher[0],
                    "encryption_bits": cipher[2],
                    "subject": dict(x[0] for x in cert.get('subject', [])),
                    "issuer": dict(x[0] for x in cert.get('issuer', []))
                }
                print(json.dumps(result, indent=2))
                return result
    except Exception as e:
        print(f"[-] TLS probe failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "example.com"
    probe_tls(target)
  
