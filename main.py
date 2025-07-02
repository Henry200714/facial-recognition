import cv2

face_haar_cascade = cv2.cascadeclassifer('haarcascade_frontal face_defualt.xml')
image=cv2.imread(demo.jpeg)
gray=cv2.cvtcolor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitkey()
faces =face_haar_cascade.detectMultiscale (gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangel(image,(x,y),(x+w,y+h)),
           ((0,255,0),5)
    cv2.imshow("faces",image)
    cv2.waitkey()