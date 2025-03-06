import cv2
img=cv2.imread('lena23.png',1)
img=cv2.line(img,(0,0),(255,255),(0,0,255),3)
img=cv2.arrowedLine(img,(0,255),(255,255),(0,0,255),3)
img=cv2.rectangle(img,(384,0),(510,128),(0,0,255),3)
img=cv2.circle(img,(200,350),50,(0,255,0),2)
f=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'opencv',(203,300),f,4,(0,0,255),10,cv2.LINE_4)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()