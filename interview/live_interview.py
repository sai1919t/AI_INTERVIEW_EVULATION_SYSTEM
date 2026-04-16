import cv2
import time
import threading
import sounddevice as sd
import soundfile as sf
import numpy as np
import os
# ----------------------------
# AUDIO RECORDING WITH MANUAL STOP
# ----------------------------

def record_audio_manual_stop(filename, stop_flag, fs=16000):

    print("Recording... Press 'S' in camera window to stop.")

    recording = []

    def callback(indata, frames, time_info, status):
        if stop_flag["stop"]:
            raise sd.CallbackStop()
        recording.append(indata.copy())

    try:
        with sd.InputStream(callback=callback, samplerate=fs, channels=1):
            while not stop_flag["stop"]:
                sd.sleep(200)
    except:
        pass

    if recording:
        audio = np.concatenate(recording)
        sf.write(filename, audio, fs)

    print("Audio recording stopped.")


# ----------------------------
# MAIN INTERVIEW FUNCTION
# ----------------------------
def conduct_interview(dept, questions):

    os.makedirs("data/recordings", exist_ok=True)

    audio_files = []
    video_files = []

    for i, question in enumerate(questions):

        print("\n--------------------------------")
        print(f"Question {i+1}: {question}")
        print("Recording started automatically...")
        print("Press 'S' to stop recording.")

        audio_file = f"data/recordings/audio_{i}.wav"
        video_file = f"data/recordings/video_{i}.avi"

        # -------- AUDIO SETUP --------
        fs = 16000
        audio_frames = []
        recording = True

        def audio_callback(indata, frames, time_info, status):
            if recording:
                audio_frames.append(indata.copy())

        stream = sd.InputStream(samplerate=fs, channels=1, callback=audio_callback)
        stream.start()

        # -------- VIDEO SETUP --------
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_FPS, 20)

        if not cap.isOpened():
            print("ERROR: Camera not accessible")
            return [], []

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(video_file, fourcc, 20.0, (640, 480))

        cv2.namedWindow("AI Interview Camera (LIVE)", cv2.WINDOW_NORMAL)

        start_time = time.time()

        # -------- RECORD LOOP --------
        while True:

            ret, frame = cap.read()
            if not ret:
                break

            elapsed = int(time.time() - start_time)

            # REC indicator
            cv2.putText(frame, "REC ●", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255), 2)

            # Timer display
            cv2.putText(frame, f"Time: {elapsed}s", (20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                        (255, 255, 255), 2)

            out.write(frame)
            cv2.imshow("AI Interview Camera (LIVE)", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('s') or key == ord('S'):
                print("Recording stopped.")
                break

        # -------- STOP EVERYTHING --------
        recording = False
        stream.stop()
        stream.close()

        cap.release()
        out.release()
        cv2.destroyAllWindows()

        # Save audio file (fast merge)
        if audio_frames:
            audio_data = np.concatenate(audio_frames, axis=0)
            sf.write(audio_file, audio_data, fs)

        audio_files.append(audio_file)
        video_files.append(video_file)

    return audio_files, video_files