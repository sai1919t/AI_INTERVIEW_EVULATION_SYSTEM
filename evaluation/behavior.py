import cv2
from deepface import DeepFace

def evaluate_behavior(video_path):

    try:
        cap = cv2.VideoCapture(video_path)

        emotions = []

        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            frame_count += 1

            # analyze every 20th frame (faster)
            if frame_count % 20 != 0:
                continue

            try:
                result = DeepFace.analyze(
                    frame,
                    actions=['emotion'],
                    enforce_detection=False
                )

                emotions.append(result[0]['dominant_emotion'])

            except:
                continue

        cap.release()

        if not emotions:
            return 5

        # 🎯 COUNT EMOTIONS
        happy = emotions.count("happy")
        neutral = emotions.count("neutral")
        sad = emotions.count("sad")
        fear = emotions.count("fear")

        total = len(emotions)

        confidence_ratio = (happy + neutral) / total

        # 🎯 SCORING
        if confidence_ratio > 0.75:
            return 8
        elif confidence_ratio > 0.5:
            return 6
        elif confidence_ratio > 0.3:
            return 5
        else:
            return 3

    except Exception as e:
        print("Behavior Error:", e)
        return 5