import numpy as np
import cv2 as cv

img = cv.imread("rice.png", cv.IMREAD_GRAYSCALE)

ret, thresh = cv.threshold(img, 120, 255, 0)

kernel = np.ones((3, 3), np.uint8)
erosion = cv.erode(thresh, kernel, iterations = 1)

img1, contours, hierarchy = cv.findContours(erosion, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
imgc = cv.cvtColor(img1, cv.COLOR_GRAY2BGR)

cv.drawContours(imgc, contours, -1, (0,0,255), 1)

print(len(contours))

cv.namedWindow('Display', cv.WINDOW_NORMAL)
cv.imshow('Display', imgc)
cv.waitKey(0)
cv.destroyAllWindows()
