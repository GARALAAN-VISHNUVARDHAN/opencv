import numpy as np
import cv2
img=cv2.imread("C:/Users/Vvish/Desktop/messi.png")
print(img.shape)#return a tuple of numbers of rows,columns,and channels
print(img.size)#return total number of pixels is accessed
print(img.dtype)#return image datatype is obtained
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
x, y, w, h = (230, 489, 60, 80)
ball=img[y:y+h,x:x+w]
new_x,new_y=400,300
img[new_y:new_y+h, new_x:new_x+w]=ball
img=cv2.resize(img,(512,512))
# to add to images
img1=cv2.imread('lena23.png')
img1=cv2.resize(img1,(512,512))
dst=cv2.addWeighted(img,.7,img1,.3,0)
cv2.imshow('image',dst)
cv2.waitKey(0)

cv2.destroyAllWindows()
