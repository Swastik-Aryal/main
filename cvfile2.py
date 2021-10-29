import cv2 as cv
import numpy as np
import time

blank = np.zeros((500,500,3), dtype = "uint8")
#cv.imshow("lol", blank)
#cv.waitKey(0)
blank[:] = (0,0,255)

def haha():
    cv.imshow("lol", blank)
    cv.waitKey(1000)

cv.rectangle(blank,((blank.shape[0]//2)//2,(blank.shape[1]//2)//2),((blank.shape[0] - (blank.shape[0]//2)//2),(blank.shape[1] - (blank.shape[1]//2)//2)),(0,255,0), thickness = 3)
haha()

cv.line(blank,((blank.shape[0]//2)//2,(blank.shape[1]//2)//2),((blank.shape[0] - (blank.shape[0]//2)//2),(blank.shape[1] - (blank.shape[1]//2)//2)), (255,100,100), thickness = 2)
haha()

cv.line(blank, ((blank.shape[0] - (blank.shape[0]//2)//2), (blank.shape[1]//2)//2), ((blank.shape[0]//2)//2, (blank.shape[1] - (blank.shape[1]//2)//2)), (225,100,100),thickness = 2)
haha()

cv.circle(blank, ((blank.shape[0]//2),(blank.shape[1]//2)), 176, (255,0,240), thickness=2 )
cv.imshow("lol", blank)
cv.waitKey(0)

