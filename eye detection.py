import cv2

eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    eyes=eye_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow('th',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

#img = cv2.imread('lena.jpg')
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#faces=face_cascade.detectMultiScale(gray,1.1,4)

#for (x,y,w,h) in faces:
#    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

#cv2.imshow("gvhg",img)
