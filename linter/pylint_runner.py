import subprocess
import json

def run_pylint(filepath):
    try:
        result = subprocess.run(
            ["pylint", filepath, "-f", "json"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        # Handle syntax errors (which appear in stderr)
        if result.stderr and not result.stdout:
            return [{
                "type": "error",
                "message": result.stderr.strip()
            }]
        return json.loads(result.stdout or "[]")
    except Exception as e:
        return [{
            "type": "error",
            "message": f"Exception while running pylint: {str(e)}"
        }]
