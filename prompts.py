evaluation_prompt = """
You are a technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Expected Concept:
{expected}

Evaluate the candidate answer and provide:

1. Score out of 10
2. Feedback
3. Suggestion for improvement
"""