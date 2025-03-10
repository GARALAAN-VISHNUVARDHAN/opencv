import numpy as np
import cv2
# events=[i for i in dir(cv2) if 'EVENT' in i]
# print(events)
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_FLAG_LBUTTON:
        print(x,',',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strxy=str(x)+','+str(y)
        cv2.putText(img,strxy,(x,y),font,1,(255,255,0),1)#this print the mouseleftclick coordinates in the img
        cv2.imshow('image',img)
    if event==cv2.EVENT_RBUTTONDBLCLK:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv2.FONT_HERSHEY_SIMPLEX
        strbgr=str(blue)+','+str(green)+','+str(red)
        cv2.putText(img,strbgr,(x,y),font,1,(0,255,255),1)#this print the mouserightclick coordinates in the img
        cv2.imshow('image',img)
img=cv2.imread("C:/Users/Vvish/Desktop/messi.png")
cv2.imshow("image",img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()