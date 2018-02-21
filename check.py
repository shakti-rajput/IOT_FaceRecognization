import ssl
import face_recognition
import urllib.request
import cv2
import os
from PIL import Image
import webbrowser
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
path1 = '/home/pi/Desktop/xyz/Desktop/face_recog/pics'

def getImageWithId(path):
     imagePaths = [os.path.join(path ,f) for f in os.listdir(path)]
     print(imagePaths)

getImageWithId(path1)
    
    
    
               
    
