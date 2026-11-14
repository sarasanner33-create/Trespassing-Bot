#!/usr/env/python3
"""
Script 01: Environment Validation
Verifies sandbox isolation, non-root execution, and security flags.
"""

import os
import sys

def check_environment():
    print("[*] Validating TrespassingBot sandbox environment...")
    
    # 1. Check UID (Must not be root)
    uid = os.geteuid()
    if uid == 0:
        print("[!] WARNING: Running as root! Sandbox container should drop privileges.")
        is_safe = False
    else:
        print(f"[+] Privilege check passed: Running as UID {uid} (non-root).")
        is_safe = True

    # 2. Check for container indicators or cgroups
    if os.path.exists("/proc/1/cgroup"):
        with open("/proc/1/cgroup", "r") as f:
            content = f.read()
            if "docker" in content or "kubepods" in content or "containerd" in content:
                print("[+] Containerized execution environment confirmed.")
            else:
                print("[!] Notice: Environment does not show standard container cgroups.")

    # 3. Verify Python version
    py_version = sys.version_info
    print(f"[+] Python runtime: {py_version.major}.{py_version.minor}.{py_version.micro}")

    if is_safe:
        print("[+] Environment validation successful.")
        sys.exit(0)
    else:
        print("[-] Environment validation failed security thresholds.")
        sys.exit(1)

if __name__ == "__main__":
    check_environment()
