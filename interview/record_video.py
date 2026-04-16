import cv2
import time

def record_video(filename, duration=20):
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

    start = time.time()
    while int(time.time() - start) < duration:
        ret, frame = cap.read()
        if not ret:
            break

        out.write(frame)
        cv2.imshow("Interview Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
