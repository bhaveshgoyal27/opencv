import matplotlib.pylab as plt
import cv2
import numpy as np

image = cv2.imread('road.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (0, height),
    (width/2, height/2),
    (width, height)
]

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

#cropped_image = region_of_interest(image,np.array([region_of_interest_vertices], np.int32),)


gray_image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
canny_image=cv2.Canny(gray_image,100,200)

cropped_image = region_of_interest(canny_image,
                np.array([region_of_interest_vertices], np.int32),)

lines=cv2.HoughLinesP(cropped_image,rho=6,theta=np.pi/60,threshold=160,lines=np.array([]),
                      minLineLength=40,maxLineGap=25)

for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)

plt.imshow(cropped_image)
plt.imshow(image)
plt.show()
