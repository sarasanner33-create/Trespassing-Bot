"""
Sysadmin Footprint Monitor
Tracks CPU, memory, threads, and file handles during sandbox execution.
"""

import os
import psutil
import json

def capture_system_footprint():
    """Captures the immediate system footprint of the current process."""
    try:
        process = psutil.Process(os.getpid())
        
        footprint = {
            "pid": process.pid,
            "cpu_percent": process.cpu_percent(interval=0.05),
            "memory_rss_mb": round(process.memory_info().rss / (1024 * 1024), 2),
            "memory_vms_mb": round(process.memory_info().vms / (1024 * 1024), 2),
            "open_files_count": len(process.open_files()),
            "active_threads": process.num_threads(),
            "status": process.status()
        }
        return footprint
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    print(json.dumps(capture_system_footprint(), indent=2))
  
