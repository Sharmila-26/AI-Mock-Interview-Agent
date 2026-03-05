from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def evaluate_answer(user_answer, correct_answer):

    embeddings = model.encode([user_answer, correct_answer])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    score = float(round(similarity * 10,2))

    return score
