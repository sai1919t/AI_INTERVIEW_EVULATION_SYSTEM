from sentence_transformers import SentenceTransformer, util

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def evaluate_knowledge(user_answers, questions):

    total_score = 0
    weak_topics = []

    for i, q in enumerate(questions):

        user_ans = user_answers[i].strip()

        if not user_ans:
            weak_topics.append(q["question"])
            continue

        correct_answers = q["answers"]

        # Encode user answer
        user_embedding = model.encode(user_ans, convert_to_tensor=True)

        max_similarity = 0

        # Compare with all correct answers
        for ans in correct_answers:
            ans_embedding = model.encode(ans, convert_to_tensor=True)

            similarity = util.cos_sim(user_embedding, ans_embedding).item()

            if similarity > max_similarity:
                max_similarity = similarity

        # 🔥 Convert similarity → score
        score = max_similarity * 10
        total_score += score

        # Weak if low similarity
        if max_similarity < 0.5:
            weak_topics.append(q["question"])

    avg_score = total_score / len(questions)

    return round(avg_score, 2), weak_topics