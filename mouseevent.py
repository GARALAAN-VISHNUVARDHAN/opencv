import numpy as np
import cv2
def click_event(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),15,(0,0,255),1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-1],(255,0,0),5)
        cv2.imshow("image",img)



#img=cv2.imread('lena23.png')
img=np.zeros((512,512,3),np.uint8)
cv2.imshow("image",img)
points=[]
cv2.setMouseCallback("image",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()