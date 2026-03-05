AI Mock Interview Agent

Overview

The AI Mock Interview Agent is an intelligent interview practice system that evaluates candidate responses using Natural Language Processing (NLP). The system simulates a real interview environment by presenting questions, analyzing user responses, generating scores, and providing feedback to help candidates improve their answers.

This project demonstrates the use of AI, embeddings, and similarity-based evaluation to automate interview assessment.

Features

AI-based interview question system

Automatic answer evaluation using semantic similarity

Score generation for each response

Real-time feedback generation

Interview progress tracking

Final performance summary after completing all questions

Technologies Used

Python

Flask

Sentence Transformers

Scikit-learn

HTML

CSS

JavaScript

How It Works

The system displays an interview question.

The user submits their answer.

The answer is converted into embeddings using Sentence Transformers.

Cosine similarity is calculated between the user answer and the reference answer.

A score and feedback are generated.

After completing all questions, the system produces an overall performance summary.

Future Improvements

RAG-based dynamic question retrieval

Advanced AI feedback generation

Interview analytics dashboard

Voice-based interview interaction

Cloud deployment

