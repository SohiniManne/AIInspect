# 🧠 AIInspect 

It uses Python, Flask, and Pylint to provide static code analysis and basic AI-based suggestions for submitted Python code.

---

## 🚀 Features

- Accepts Python code via a POST API
- Analyzes the code using **Pylint**
- Returns linting issues and basic AI-generated feedback
- CORS-enabled to work with frontend (React or other)

---

## 📁 Project Structure
AIInspect/
│
├── app/
│ ├── init.py
│ ├── routes.py # Main Flask route logic
│ └── review.py # Core logic for code analysis
│
├── ai_engine/
│ └── openai_engine.py # (Optional) AI feedback integration (mocked or OpenAI)
│
├── venv/ # Virtual environment (not pushed to Git)
│
├── run.py # Entry point to run the Flask app
├── requirements.txt # Python dependencies
└── README.md # This file


---

 🛠️ Installation

1. Clone the repository
   ```bash
   git clone https://github.com/SohiniManne/AIInspect.git
   cd AIInspect

2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # For Windows

3. Install dependencies
pip install -r requirements.txt

4. Install Pylint manually
   pip install pylint


