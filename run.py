from app.routes import app

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test-review', methods=['POST'])
def test_review():
    data = request.get_json()
    code = data.get("code", "")
    
    # Mock feedback (replace with your actual logic)
    return jsonify({
        "ai_feedback": "- Use meaningful variable names\n- Add docstring to your function\n- Consider error handling",
        "lint_issues": []
    })

if __name__ == "__main__":
    app.run(debug=True)
