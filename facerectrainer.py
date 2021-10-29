import cv2 as cv
import numpy as np
import os

# people=[]
# for i in os.listdir("D:\peoples"):
#     people.append(i)
# print (people)
people = ["alexandra","chris evans","vin diesel"]
Dir = r"D:\people"
haar_cascade = cv.CascadeClassifier("haar_facedetect.xml")

features = []
labels = []

def create_trainer():
    for person in people:
        path = os.path.join(Dir,person)
        label = people.index(person)

        for image in os.listdir(path):
            img_path = os.path.join(path,image)
            img = cv.imread(img_path)
            grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            face = haar_cascade.detectMultiScale(grey,1.1,4)
            for(x,y,a,b) in face:
                face_need = grey[y:y+b,x:x+a]
                features.append(face_need)
                labels.append(label)

create_trainer()

features = np.array(features, dtype="object")
labels = np.array(labels)



face_recognition = cv.face.LBPHFaceRecognizer_create()
face_recognition.train(features,labels)

face_recognition.save("face_Recog.yml")
np.save("features",features)
np.save("labels",labels)


# img = cv.imread(r"D:\people\chris evans\chris.jpg")
# cv.imshow("img",img)
# cv.waitKey(0)