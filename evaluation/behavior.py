from deepface import DeepFace
import cv2

def evaluate_behavior(video_path):

    cap = cv2.VideoCapture(video_path)

    emotion_counter = {
        "happy": 0,
        "neutral": 0,
        "fear": 0,
        "sad": 0,
        "angry": 0
    }

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % 30 == 0:  # analyze every 30th frame
            try:
                result = DeepFace.analyze(
                    frame,
                    actions=['emotion'],
                    enforce_detection=False
                )

                emotion = result[0]['dominant_emotion']

                if emotion in emotion_counter:
                    emotion_counter[emotion] += 1

            except:
                pass

        frame_count += 1

    cap.release()

    total = sum(emotion_counter.values())

    if total == 0:
        return 0

    confidence = (
        emotion_counter["happy"] +
        emotion_counter["neutral"]
    ) / total

    return round(confidence * 10, 2)