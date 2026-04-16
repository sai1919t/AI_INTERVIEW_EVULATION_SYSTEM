import librosa
import numpy as np

def evaluate_speech(audio_path, transcripts):

    y, sr = librosa.load(audio_path)

    duration = librosa.get_duration(y=y, sr=sr)

    total_words = sum(len(t.split()) for t in transcripts if t.strip())

    if duration == 0 or total_words == 0:
        return 0

    words_per_minute = (total_words / duration) * 60

    # Ideal speaking rate = 120–160 WPM
    if 120 <= words_per_minute <= 160:
        fluency_score = 10
    elif 100 <= words_per_minute <= 180:
        fluency_score = 8
    else:
        fluency_score = 5

    fillers = ["um", "uh", "like", "actually", "you know"]
    filler_count = sum(
        t.lower().split().count(f)
        for t in transcripts
        for f in fillers
    )

    filler_penalty = min(3, filler_count * 0.3)

    final_score = max(0, fluency_score - filler_penalty)

    return round(final_score, 2)