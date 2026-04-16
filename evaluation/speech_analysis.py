import re

FILLER_WORDS = ["um", "uh", "like", "actually", "basically"]

def evaluate_speech(transcripts):

    total_wpm = 0
    total_fillers = 0

    for text in transcripts:
        words = text.split()
        word_count = len(words)

        # 20 sec answer → approximate WPM
        wpm = word_count * 3
        total_wpm += wpm

        lower = text.lower()
        for filler in FILLER_WORDS:
            total_fillers += len(re.findall(r'\b' + filler + r'\b', lower))

    avg_wpm = total_wpm / len(transcripts)

    if 110 <= avg_wpm <= 160:
        speech_score = 8
    else:
        speech_score = 6

    penalty = min(total_fillers * 0.2, 2)

    final_score = max(speech_score - penalty, 0)

    return round(final_score, 2), avg_wpm, total_fillers