import cv2
import time
from hand import HandTracker as hand_track

cap=cv2.VideoCapture(0);
h=hand_track()

while True:
    ret,frame=cap.read()
    frame,res=h.find_hands(frame)
    lmlist=h.find_landmarks(frame,res)
    if len(lmlist)!=0:
        for ha in lmlist:
            if len(ha)>8:
            
                print(ha[4],ha[8])
    cv2.imshow('image',frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
       break 

cap.release()
cv2.destroyAllWindows()