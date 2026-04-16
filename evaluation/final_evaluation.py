from evaluation.knowledge import evaluate_knowledge
from evaluation.speech import evaluate_speech
from evaluation.behavior import evaluate_behavior
from utils.audio_utils import extract_audio
import os

def evaluate_all(user_answers, questions, video_path, transcripts):

    knowledge_score, weak_topics = evaluate_knowledge(user_answers, questions)

    audio_path = video_path.replace(".mp4", ".wav")
    extract_audio(video_path, audio_path)

    speech_score = evaluate_speech(audio_path, transcripts)
    behavior_score = evaluate_behavior(video_path)

    # Weighted Final Score
    final_score = round(
        (0.5 * knowledge_score) +
        (0.25 * speech_score) +
        (0.25 * behavior_score),
        2
    )

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