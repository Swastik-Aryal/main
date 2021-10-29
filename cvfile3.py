import cv2 as cv
import numpy as np
import random

blank = np.zeros((500,500,3), dtype = "uint8")

for i in range(245):
    cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),i+5,(random.randint(1,255),random.randint(1,255),random.randint(1,255)),thickness=2)
    cv.imshow("Circles",blank)
    cv.waitKey(200)


cv.imshow("Circles",blank)
cv.waitKey(0)