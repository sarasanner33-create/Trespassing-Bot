"""
Sandbox API Execution Runner
Spawns subprocesses within strict operating limits (processes, memory, file size).
"""

import subprocess
import json
import sys

def execute_sandboxed_command(cmd_list: list, timeout_sec: int = 5):
    """
    Executes a command with prlimit restrictions:
    - Max processes (--nproc=30)
    - Max address space memory (--as=200MB)
    - Max file write size (--fsize=1MB)
    """
    restricted_cmd = [
        "prlimit",
        "--nproc=30",
        "--as=200000000",
        "--fsize=1048576"
    ] + cmd_list

    try:
        result = subprocess.run(
            restricted_cmd,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            check=False
        )
        return {
            "exit_code": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip()
        }
    except subprocess.TimeoutExpired:
        return {"error": "Execution timed out in sandbox runner."}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python runner.py <command> [args...]बाड़ी")
        sys.exit(1)
    
    output = execute_sandboxed_command(sys.argv[1:])
    print(json.dumps(output, indent=2))
      
