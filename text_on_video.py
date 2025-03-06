import cv2
import datetime
cap=cv2.VideoCapture(0);
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap.set(3,700)
cap.set(4,700)
print(cap.get(3))
print(cap.get(4))

while(cap.isOpened):
    ret,frame=cap.read()
    if ret==True:
        f=cv2.FONT_HERSHEY_SIMPLEX
        text='width:'+str(cap.get(3)) + 'height:' + str(cap.get(4))
        date=str(datetime.datetime.now())
        frame=cv2.putText(frame,date,(20,50),f,1,(0,255,255),2,cv2.LINE_AA)#(20=x axis,50=yaxis) from top to bottom
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1)&0xFF==ord('q'):
            break
    else:
        break
cap.release()

cv2.destroyAllWindows()
