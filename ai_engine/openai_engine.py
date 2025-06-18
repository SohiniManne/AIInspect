import os
import openai
from openai import OpenAI

# Load your OpenAI API key from an environment variable or directly
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_ai_review(code: str) -> str:
    # placeholder logic
    return "AI review: Looks good overall. Add comments and use descriptive names."


    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=prompt
        )

        message = response.choices[0].message.content.strip()
        return message

    except Exception as e:
        return f"AI review failed: {str(e)}"
