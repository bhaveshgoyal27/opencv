import cv2
import numpy as np

#img=cv2.imread('opencv-logo.png')
img=cv2.imread('lena.jpg')
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernal=np.ones((5,5),np.uint8)
dst=cv2.filter2D(img,-1,kernal)
blur=cv2.blur(img,(5,5))
gblur=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img,5)
bilateralF=cv2.bilateralFilter(img,9,75,75)

t=['images','dst','blur','gblur','median','bilateralF']
im=[img,dst,blur,gblur,median,bilateralF]

for i in range(len(t)):
    cv2.imshow(t[i],im[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
