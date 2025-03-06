import cv2
import mediapipe as mp
cap=cv2.VideoCapture(0);
mpHands= mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
while True:
    ret,frame=cap.read()
    imgrgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(imgrgb)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # for id,lm in enumerate(handLms.landmark):
            #     #print(id,lm)
            #     h,w,c=frame.shape
            #     cx,cy=int(lm.x*w),int(lm.y*h)
            #     if id==8:# 4,8,12,16,20
            #         cv2.circle(frame,(cx,cy),10,(255,0,0),-1)
            mpDraw.draw_landmarks(frame,handLms,mpHands.HAND_CONNECTIONS)
    cv2.imshow('image',frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()