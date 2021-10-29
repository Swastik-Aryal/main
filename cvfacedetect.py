import cv2 as cv

# img = cv.imread("D:/images/aryalji.jpg")
# resized = cv.resize(img,(img.shape[0]//7,img.shape[1]//4))
# # cv.imshow("me",resized)
#
# gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
#
# haar_cascade = cv.CascadeClassifier("haar_facedetect.xml")
#
# faces = haar_cascade.detectMultiScale(gray  ,scaleFactor=1.1, minNeighbors=8)
#
# for (x,y,a,b) in faces:
#     cv.rectangle(resized,(x,y),(x+a,y+b), (0,255,0)   ,thickness=2)
# cv.imshow("face_detct", resized)
#
# cv.waitKey(0)


vid = cv.VideoCapture(0)
# address = "https://192.168.1.66:8080/video"
# vid.open(address)

def face_detect(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier("haar_facedetect.xml")
    faces = haar_cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors=3 )
    for (x,y,a,b) in faces:
        cv.rectangle(img,(x,y),(x+a,y+b),(0,255,0),2)
    return img
def smile_detect(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier("haar_smiledetect.xml")
    smiles = haar_cascade.detectMultiScale(gray,scaleFactor=3.5,minNeighbors=20)
    for (x,y,a,b) in smiles:
        cv.rectangle(img,(x,y),(x+a,y+b),(0,255,0),2)
    return img

while True:
    isTrue, frame = vid.read()

    flipped=cv.flip(frame,1)
    cv.imshow("face_detection",smile_detect(flipped))
    key = cv.waitKey(1)

    if key == ord("c"):
        break
vid.release()
cv.destroyAllWindows()
