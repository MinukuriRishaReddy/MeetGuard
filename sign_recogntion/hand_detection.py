# src/sign_recognition/hand_detection.py
import cv2
import mediapipe as mp

class HandGestureRecognizer:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False, max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils

    def detect_gestures(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
            return results.multi_hand_landmarks
        return None

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    recognizer = HandGestureRecognizer()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        recognizer.detect_gestures(frame)
        cv2.imshow("Hand Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
