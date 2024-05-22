#Face recognition model
#mini project
#import necessary modules
from google.colab.patches import cv2_imshow
import cv2

#use pretrained model
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

#Load the image into this model
image=cv2.imread('friends.jpg')#uploaded file name.type

#convert image to gray scale image

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Detect faces
faces=face_cascade.detectMultiScale(gray,scaleFactor=1.8)

#Draw a rectangle around the face
for (x,y,w,h) in faces:
  cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0,),2)

cv2_imshow(image)

