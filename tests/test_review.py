# Complete corrected version of your test_review.py file:

import json
import subprocess
import tempfile
from flask import Flask, request, jsonify

# Option 1: Create a new Flask app instance (for standalone testing)
app = Flask(__name__)

# Option 2: OR import from your main app file (uncomment and modify as needed)
# from main import app  # Replace 'main' with your actual main file name
# from app import app   # If your main file is named app.py
# from server import app # If your main file is named server.py

@app.route('/test-review', methods=['POST'])
def test_review():
    data = request.get_json()
    code = data.get("code", "")

    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as tmp:
        tmp.write(code)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            ["pylint", tmp_path, "-f", "json"],
            capture_output=True,
            text=True,
            check=False
        )

        if not result.stdout and result.stderr:
            lint_results = [{"type": "error", "message": result.stderr.strip()}]
        else:
            lint_results = json.loads(result.stdout or "[]")

    except Exception as e:
        lint_results = [{"type": "error", "message": f"Pylint failed: {str(e)}"}]

    ai_feedback = []
    if "def" in code:
        ai_feedback.append("- Add docstring to your function")
    if any(var in code for var in ["x", "y", "z"]):
        ai_feedback.append("- Use more descriptive variable names")

    response_payload = {
        "lint_issues": lint_results,
        "ai_feedback": "\n".join(ai_feedback) or "No suggestions 🎉"
    }
    print("Response payload:", response_payload)
    return jsonify(response_payload)

# If running as standalone test
if __name__ == '__main__':
    app.run(debug=True)