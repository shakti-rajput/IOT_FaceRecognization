import ssl
import urllib.request
import cv2
import webbrowser
import numpy as np
url = 'http://192.168.43.27:8080/shot.jpg'
import pymysql
conn=pymysql.connect(host='sql12.freesqldatabase.com',user='sql12223390',password='rztsUtEH2t',db='sql12223390')
a=conn.cursor()



cascadePath = "/home/pi/Desktop/xyz/Desktop/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

ID = input('Enter ID for recognition ')
name = input('Enter name for recognition ')
age = input('Enter age for recognition ')
sql=("INSERT INTO Person (Id,Name,Age) VALUES ('%s', '%s', '%s')" % (ID,name,age))
#insertstmt=("insert into TBLB (dateK, id, name, city) values ('%s', '%s', '%s', '%s')" % (dateK, id, name, city))
#insertstmt=("insert into TBLB (dateK, id, name, city) values ('%s', '%s', '%s', '%s')"
a.execute(sql)
conn.commit()

samplenum = 0
while True:
    #print("shakti")
    context = ssl._create_unverified_context()
    res = urllib.request.urlopen(url,context = context)
    imgNp = np.array(bytearray(res.read()) , dtype = np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.imdecode(imgNp,-1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.3,5)
    #print("shakti")
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        samplenum+=1
        cv2.imwrite('/home/pi/Desktop/xyz/Desktop/face_recog/pics/img.'+ID + '.' + str(samplenum) + ".jpg" , gray[y:y+h , x:x+w])
        cv2.waitKey(100)
        
        
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
          #  cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('img',img)
    if (samplenum > 40):
        break
    #cv2.imshow('test' , img)
    #cv2.imshow('gray' , gray)
   # cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()