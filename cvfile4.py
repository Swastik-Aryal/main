import cv2 as cv
import numpy as np
'''
img = cv.imread("D:/images/rose.png")
cv.imshow("normal", img)

greyme = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", greyme)

#edge cascade
cas = cv.Canny(img,175,200)
cv.imshow("edges", cas)

#resizing
resized = cv.resize(img, (700,700))
cv.imshow("res", resized)

#CROP
cropped = img[240:270, 100:500]
cv.imshow("croppedimg", cropped)

#flipping
flipped = cv.flip(img,1)
cv.imshow("flipped image",flipped)


cv.waitKey(0)
'''


myvid = cv.VideoCapture(0)

while True:
    isTrue, frame = myvid.read()

    flipped = cv.flip(frame,-1)

    #cas = cv.Canny(frame,25,75)

    cv.imshow("video", flipped)
    cv.waitKey(20)

    if 0xFF == ord('c'):
        break



myvid.release()
cv.destroyAllWindows()

