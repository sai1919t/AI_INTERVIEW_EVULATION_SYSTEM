import whisper
import os

model = whisper.load_model("base")

def transcribe_audio(file_path):

    if not os.path.exists(file_path):
        return ""

    if os.path.getsize(file_path) < 2000:
        return ""

    try:
        result = model.transcribe(file_path)
        text = result.get("text", "").strip()
        return text
    except Exception as e:
        print("Whisper error:", e)
        return ""