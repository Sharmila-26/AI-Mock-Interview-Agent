import json
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.Client()

collection = client.create_collection("interview_questions")


def load_questions():

    with open("question_bank.json","r") as f:
        data = json.load(f)

    for i,item in enumerate(data):

        embedding = model.encode(item["question"]).tolist()

        collection.add(
            ids=[str(i)],
            documents=[item["question"]],
            embeddings=[embedding],
            metadatas=[item]
        )


def retrieve_question(topic):

    results = collection.query(
        query_texts=[topic],
        n_results=1
    )

    return results["metadatas"][0][0]