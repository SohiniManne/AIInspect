import subprocess
import json


def review_code(code: str):
    # Your pylint + AI logic here
    return {
        "lint_issues": [...],
        "ai_feedback": "..."
    }


def run_pylint(filepath):
    try:
        result = subprocess.run(
            ["pylint", filepath, "-f", "json"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )

        # ⚠️ If syntax error, it's usually only in stderr
        if result.stderr and not result.stdout:
            return [{
                "type": "error",
                "message": result.stderr.strip()
            }]

        # Return parsed results if possible
        return json.loads(result.stdout or "[]")

    except Exception as e:
        return [{
            "type": "error",
            "message": f"Pylint failed: {str(e)}"
        }]
