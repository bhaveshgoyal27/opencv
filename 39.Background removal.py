import numpy as np
import cv2
cap=cv2.VideoCapture('vtest.avi')
#fgbg=cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg=cv2.createBackgroundSubtractorMOG2()
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
while True:
    ret,frame= cap.read()
    if frame is None:
        break
    fgmask=fgbg.apply(frame)
    fgmask=cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,kernel)
    
    cv2.imshow('Frame',frame)
    cv2.imshow('segm1',fgmask)

    keyboard=cv2.waitKey(30)
    if keyboard =='q' or keyboard ==27:
        break
cap.release()
cv2.destroyAllWindows()
