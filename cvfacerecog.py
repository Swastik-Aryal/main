import cv2 as cv
import numpy as np

people = ["alexandra", "chris evans", "vin diesel"]

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_Recog.yml")

haar_cascade = cv.CascadeClassifier("haar_facedetect.xml")

img = cv.imread(r"D:\1234.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face = haar_cascade.detectMultiScale(gray, 1.1, 5)

for (x, y, a, b) in face:
    face_req = gray[y:y + b, x:x + a]
    label,confidence=face_recognizer.predict(face_req)
    print(str(people[label]),(confidence))
    cv.rectangle(img, (x, y), (x + a, y + b), (0, 255, 0), 2)
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0))
cv.imshow("img", img)
cv.waitKey(0)
