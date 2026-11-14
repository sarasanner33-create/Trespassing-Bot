#!/usr/env/python3
"""
Script 06: Mask Verification
Tests whether sensitive host/kernel paths are successfully masked (unreadable or empty).
"""

import sys
import os

MASKED_TARGETS = [
    "/proc/kcore",
    "/proc/keys",
    "/proc/timer_list",
    "/sys/firmware",
    "/proc/acpi"
]

def verify_masks():
    print("[*] Verifying container footprint masks...")
    failures = 0

    for path in MASKED_TARGETS:
        if not os.path.exists(path):
            print(f"[+] PASSED: {path} does not exist or is fully hidden.")
            continue
            
        try:
            # Try to open or stat the masked path
            with open(path, "r") as f:
                content = f.read(10)
                print(f"[!] WARNING: {path} is readable! Content preview: {content}")
                failures += 1
        except Exception as e:
            # Expected behavior for masked/unreadable paths
            print(f"[+] PASSED: {path} is successfully masked (Access denied / error: {e})")

    if failures == 0:
        print("[+] All system footprint masks verified successfully.")
        sys.exit(0)
    else:
        print(f"[-] Mask verification failed: {failures} sensitive path(s) exposed.")
        sys.exit(1)

if __name__ == "__main__":
    verify_masks()
              
