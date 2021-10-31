import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)
_,mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernal=np.ones((2,2),np.uint8)

dilation=cv2.dilate(mask,kernal,iterations=3)
erosion=cv2.erode(mask ,kernal,iterations=5)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)

t=['image','mask','dilation','erosions','opening','closing']
im=[img,mask,dilation,erosion,opening,closing]



for i in range(len(t)):
    cv2.imshow(t[i],im[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
    
