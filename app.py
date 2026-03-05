from flask import Flask, render_template, request, jsonify
from evaluation import evaluate_answer
from rag_pipeline import load_questions, retrieve_question
from ai_feedback import generate_feedback

app = Flask(__name__)

# Load questions into vector database
load_questions()

# Interview state variables
question_index = 0
interview_history = []
questions = []


@app.route("/")
def home():

    global questions, question_index, interview_history

    # Reset interview
    interview_history = []
    question_index = 0

    # Load interview questions
    questions = [
        retrieve_question("python"),
        retrieve_question("machine_learning"),
        retrieve_question("frontend")
    ]

    return render_template(
        "index.html",
        question=questions[question_index]["question"]
    )


@app.route("/submit_answer", methods=["POST"])
def submit_answer():

    global question_index

    user_answer = request.json["answer"]

    correct_answer = questions[question_index]["answer"]

    # Evaluate answer
    score = round(float(evaluate_answer(user_answer, correct_answer)), 2)

    feedback = generate_feedback(
    questions[question_index]["question"],
    user_answer,
    score
    )

    # Save interview history
    interview_history.append({
        "question": questions[question_index]["question"],
        "score": score
    })

    question_index += 1

    
    if question_index < len(questions):

        return jsonify({
            "score": score,
            "feedback": feedback,
            "next_question": questions[question_index]["question"]
        })

    else:

        
        avg_score = round(sum(q["score"] for q in interview_history) / len(interview_history), 2)

        return jsonify({
            "score": score,
            "feedback": feedback,
            "interview_complete": True,
            "average_score": round(avg_score,2)
        })


if __name__ == "__main__":
    app.run(debug=True)