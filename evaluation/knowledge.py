from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def evaluate_knowledge(user_answers, questions):

    scores = []
    weak_topics = []

    for q_obj, user_answer in zip(questions, user_answers):

        question_text = q_obj.get("question", "")
        reference_answers = q_obj.get("answers", [])

        if not user_answer.strip():
            scores.append(0)
            weak_topics.append(question_text)
            continue

        student_embedding = model.encode(user_answer, convert_to_tensor=True)
        reference_embeddings = model.encode(reference_answers, convert_to_tensor=True)

        similarities = util.cos_sim(student_embedding, reference_embeddings)
        best_score = float(similarities.max())

        score = round(max(best_score, 0) * 10, 2)

        scores.append(score)

        if score < 5:
            weak_topics.append(question_text)

    avg_score = round(np.mean(scores), 2) if scores else 0

    return avg_score, weak_topics