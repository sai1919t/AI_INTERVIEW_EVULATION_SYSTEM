import re

def evaluate_speech(audio_path, transcripts):

    text = " ".join(transcripts).lower()

    words = text.split()
    total_words = len(words)

    if total_words == 0:
        return 0

    # 🎯 FILLER WORDS
    fillers = ["um", "uh", "like", "you know", "aaa", "hmm"]
    filler_count = sum(text.count(f) for f in fillers)

    filler_ratio = filler_count / total_words

    # 🎯 WORD VARIETY
    unique_words = len(set(words))
    diversity = unique_words / total_words

    # 🎯 SCORING
    score = 7

    # penalty
    if filler_ratio > 0.05:
        score -= 2
    if filler_ratio > 0.1:
        score -= 2

    # bonus
    if diversity > 0.6:
        score += 2

    return max(0, min(score, 10))