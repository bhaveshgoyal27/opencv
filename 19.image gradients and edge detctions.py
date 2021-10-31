import cv2
import numpy as np

#img=cv2.imread("messi5.jpg",cv2.IMREAD_GRAYSCALE)
img=cv2.imread("sudoku.png",cv2.IMREAD_GRAYSCALE)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)# used for negative nos
lap=np.uint8(np.absolute(lap))
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1)

lap=np.uint8(np.absolute(sobelx))
lap=np.uint8(np.absolute(sobely))

sobelCombined = cv2.bitwise_or(sobelx, sobely)

t=['img','lap','sobelx','sobely','sobelCombined']
im=[img,lap,sobelx,sobely,sobelCombined]

for i in range(len(t)):
    cv2.imshow(t[i],im[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
