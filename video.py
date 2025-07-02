import cv2

from main import face_haar_cascade, faces

caputre = cv2.videocapture(0)
face_haar_cascade =cv2.cascadeclassifier('haarcascade_frontalface_defualt.xml')
while true:
    _ ,image =capture.read()
    gray =cv2.cvtcolor(image,cv2.COLOR_BGR2GRAY)
    face =face_haar_cascade.detectMultiscale(gray,1.1,4)

for (x,y,w,h)in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h)),
    ((0,255,0),5)
    cv2.imshow("video",image)
    k= cv2.waitkey(30)&0xFF
    if k ==27:
        break
    cv2.realease()