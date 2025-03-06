import cv2
img=cv2.imread('c:/Users/Vvish/Pictures/Screenshots/lena.jpg.png',1)#this code raed the image in the pixels

cv2.imshow('image',img)#using this we can diplay img but in diplay in millisec
k=cv2.waitKey(0)#using this we hold that img 
if k==27:#when you press 27 img window will close
    cv2.destroyAllWindows()#this code is to close the image 
elif k==ord('s'):#when you press s it will write the img and close
    cv2.destroyAllWindows()
    cv2.imwrite('lena23.png',img)#this line is to write the image