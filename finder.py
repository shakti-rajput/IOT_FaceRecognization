import ssl
import urllib.request
import cv2
import webbrowser
import numpy as np
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
def emali(sample):
    for i in range (1,2):
        img_data = open('Desktop/email_img/img.'+str(sample)+'.jpg', 'rb').read()
        msg = MIMEMultipart()
        msg['Subject'] = 'subject'
        msg['From'] = 'shaktirajput100@gmail.com'
        msg['To'] = 'shaktirajput100@gmail.com'

        text = MIMEText("keys.text")
        msg.attach(text)
        image = MIMEImage(img_data, name=os.path.basename('ImgFileName'))
        msg.attach(image)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login('shaktirajput100@gmail.com', 'password')
        s.sendmail(msg['From'] , msg['To'], msg.as_string())
        s.quit()

#url = 'http://192.168.42.129:8080/shot.jpg'
recognizer = cv2.face.LBPHFaceRecognizer_create(2, 2, 7, 7, 15) 
#recognizer = cv2.face.LBPHFaceRecognizer_create()
print(recognizer)
recognizer.read('/home/pi/Desktop/xyz/Desktop/trainer/trainer.yml')
print(recognizer.read('/home/pi/Desktop/xyz/Desktop/trainer/trainer.yml'))
cascadePath = "/home/pi/Desktop/xyz/Desktop/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
id=0
samplenum=0
#cam = cv2.VideoCapture(0)
while True:
    context = ssl._create_unverified_context()
    res = urllib.request.urlopen("http://172.20.4.137:8080/shot.jpg",context = context)
    imgNp = np.array(bytearray(res.read()) , dtype = np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.imdecode(imgNp,-1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
        if(samplenum<2):
            samplenum+=1
            cv2.imwrite('/home/pi/Desktop/xyz/Desktop/email_img/img.'+ str(samplenum) + ".jpg" , gray[y:y+h , x:x+w])
            emali(samplenum)
        Id,conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf>=50):
            if(Id==1):
                Id="Bhatia"
                cv2.putText(img,"Prayag",(x,y-10),font,0.55,(0,255,0),1)
            elif(Id==2):
                Id="Sam"
                cv2.putText(img,"Shakti",(x,y-10),font,0.55,(0,255,0),1)
        else:
            cv2.putText(img,"Unknown",(x,y-10),font,0.55,(0,255,0),1)
        
    cv2.imshow('im',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()