import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
try:
    model = genai.GenerativeModel("gemini-pro")
except:
    model = None


def generate_feedback(question, answer, score):

    prompt = f"""
You are a technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Score: {score}/10

Provide short professional feedback explaining what was correct and what can be improved.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:

        # fallback feedback if API fails
        if score > 7:
            return "Good answer. Your explanation covers the main concept correctly."
        elif score > 4:
            return "Partially correct answer. You explained some concepts but more detail is needed."
        else:

            return "The answer is not accurate. Review the concept and include key points in your explanation."
