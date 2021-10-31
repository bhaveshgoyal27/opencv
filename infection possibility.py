import cv2
import numpy as np

def distance(a,b,c,d):
    e=(a-c)**2+(b-d)**2
    e=e**0.5
    return e

cap=cv2.VideoCapture('vtest.avi')

ret,frame1=cap.read()
ret,frame2=cap.read()

while cap.isOpened():
    diff= cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)    
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=7)
    contours,_= cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    l=[]
    n=[]
    for c in contours:
        (x,y,w,h)=cv2.boundingRect(c)
        if cv2.contourArea(c)>=800:
            x=(x+w)/2
            y=(y+h)/2
            l.append([x,y])
    for i in range(len(l)):
        m=[]
        for j in range(len(l)):
            if i!=j:
                m.append(distance(l[i][0],l[i][1],l[j][0],l[j][1]))
        if min(m)<=75:
            n.append(1)
        else:
            n.append(0)
    i=0
    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)
        if cv2.contourArea(contour)<800:
            continue
        if n[i]==1:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),2)
        else:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,"movement",(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
        i+=1

    #cv2.drawContours(frame1,contours,-1,(0,255,0),2)
    

    cv2.imshow("inter",frame1)
    frame1=frame2
    ret,frame2=cap.read()
    if cv2.waitKey(40)==27:
        break


cv2.destroyAllWindows()
cap.release()
