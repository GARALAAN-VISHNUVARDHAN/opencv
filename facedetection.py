import cv2
import time
import mediapipe as mp
cap=cv2.VideoCapture(0);
pTime=0
mpFaceDetection=mp.solutions.face_detection
mpDraw=mp.solutions.drawing_utils
faceDection=mpFaceDetection.FaceDetection(0.5)
while True:
    ret,frame=cap.read()
    imgRgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=faceDection.process(imgRgb)
    if results.detections:
        for id,detection in enumerate(results.detections):
            bboxc=detection.location_data.relative_bounding_box
            ih,iw,ic=frame.shape
            bbox=int(bboxc.xmin*iw),int(bboxc.ymin*ih),\
                int(bboxc.width*iw),int(bboxc.height*ih)
            cv2.rectangle(frame,bbox,(225,0,0),2)
            
            
            
            
            #mpDraw.draw_detection(frame,detection)

    if ret==True:
        
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(frame,f'FPS:{int(fps)}',(20,30),2,1,(255,0,0),1)
        cv2.imshow('image',frame)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
