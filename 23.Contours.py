import cv2
import numpy as np

img=cv2.imread('opencv-logo.png')
imgray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray,127,255,0)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

print(ret)
#print(thresh)
print(contours)
print(hierarchy)
print("Number of contours="+str(len(contours)))

cv2.drawContours(img,contours,-1,(255,0,255),3)


cv2.imshow("img",img)
#cv2.imshow("gray",imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()
