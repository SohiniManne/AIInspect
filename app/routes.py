from flask import Blueprint, request, jsonify
from app.review import review_code

app = Blueprint('app', __name__)

@app.route('/review', methods=['POST'])
def review():
    data = request.get_json()
    code = data.get("code", "")
    lint_issues, ai_feedback = review_code(code)
    return jsonify({
        "lint_issues": lint_issues,
        "ai_feedback": ai_feedback
    })
 