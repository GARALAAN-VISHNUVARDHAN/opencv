import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=mode, 
                                        max_num_hands=maxHands, 
                                        min_detection_confidence=detectionCon, 
                                        min_tracking_confidence=trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, frame):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(frame, handLms, self.mpHands.HAND_CONNECTIONS)

        return frame, results  # Ensure this function returns (frame, results)

    def find_landmarks(self, frame, results):
        landmark_list = []
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                hand_points = []
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    hand_points.append((id, cx, cy))
                landmark_list.append(hand_points)
        return landmark_list
