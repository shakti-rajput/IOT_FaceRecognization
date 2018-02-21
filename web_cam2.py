import ssl
import urllib.request
import cv2
import webbrowser
import numpy as np
url = 'http://192.168.42.129:8080/shot.jpg'

face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/xyz/Desktop/haarcascade_frontalface_default.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('/home/pi/Desktop/xyz/Desktop/haarcascade_eye.xml')

while True:
    context = ssl._create_unverified_context()
    res = urllib.request.urlopen("http://192.168.42.129:8080/shot.jpg",context = context)
    imgNp = np.array(bytearray(res.read()) , dtype = np.uint8)
    
    img = cv2.imdecode(imgNp,-1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    cv2.imshow('test' , img)
    cv2.imshow('gray' , gray)
   # cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
    
