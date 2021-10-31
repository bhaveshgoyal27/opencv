import cv2
import numpy as np

img=cv2.imread("sudoku.png",0)
canny=cv2.Canny(img,100,200)

t=['image','canny']
im=[img,canny]

for i in range(len(t)):
    cv2.imshow(t[i],im[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
