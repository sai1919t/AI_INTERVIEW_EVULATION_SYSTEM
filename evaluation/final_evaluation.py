from evaluation.knowledge import evaluate_knowledge
from evaluation.speech import evaluate_speech
from evaluation.behavior import evaluate_behavior
import os

def evaluate_all(user_answers, questions, video_path, transcripts):

    knowledge_score, weak_topics = evaluate_knowledge(user_answers, questions)

    if video_path and os.path.exists(video_path):
        speech_score = evaluate_speech(video_path, transcripts)
        behavior_score = evaluate_behavior(video_path)
    else:
        print("Video not found, skipping analysis")

    # ---------------- ADJUST SCORES SMARTLY ----------------

# Case 1: Weak knowledge → cap others
    if knowledge_score < 5:
        speech_score = min(speech_score, 5)
        behavior_score = min(behavior_score, 5)

# Case 2: Good knowledge → boost others slightly if too low
    else:
        if speech_score < 5:
            speech_score = 5 + (speech_score / 2)   # small boost
        if behavior_score < 5:
            behavior_score = 5 + (behavior_score / 2)

# Round values
    speech_score = round(speech_score, 2)
    behavior_score = round(behavior_score, 2)

    final_score = round((knowledge_score + speech_score + behavior_score) / 3, 2)

    if final_score >= 8:
        verdict = "Strong Hire"
    elif final_score >= 6:
        verdict = "Hire"
    elif final_score >= 4:
        verdict = "Consider"
    else:
        verdict = "Not Recommended"

    return (
        knowledge_score,
        speech_score,
        behavior_score,
        final_score,
        weak_topics,
        verdict
    )