import cv2 as cv
import time

def rescale(frame, scale = 0.75):

    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * 0.2)
    return cv.resize(frame,(width,height), interpolation = cv.INTER_AREA)
'''
img1 = cv.imread("D:/images/rose.png")
img2 = cv.imread("D:/images/blue.png")

cv.imshow("rose", rescale(img1))
cv.waitKey(0)
'''


vid = cv.VideoCapture(0)

while True:
    isTrue, frame = vid.read()
    cv.imshow("sniped", frame)

    if cv.waitKey(1) and 0xFF == ord('d'):
        break
vid.release()
cv.destroyAllWindows()

