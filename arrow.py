import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('arrow.jpg', cv.IMREAD_COLOR)
print(img)
ret, thresh = cv.threshold(img, 120, 255, 0)

im = img.crop((1, 1, 98, 33))

cv.namedWindow('Display', cv.WINDOW_NORMAL)
cv.imshow('Display', im)
cv.waitKey(0)
cv.destroyAllWindows()

