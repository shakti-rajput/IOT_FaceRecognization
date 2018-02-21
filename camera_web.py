############import urllib.request
############import cv2
############import numpy as np
############
############
############url = 'https://192.168.43.1:8080/shot.jpg'
############img = urllib.request.Request(url)
#############urllib.request.urlretrieve(url)
############res = urllib.request.urlopen(url)
#############imgNp = res.read()
#############imgNp = np.array(bytearray(img.read()), dtype = np.uint8)
##############
##########
##########


import urllib.request
import urllib.parse


url = 'https://api.spotify.com/v1/search?type=artist&q=snoop'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))
