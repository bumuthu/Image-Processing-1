import numpy as np
import cv2 as cv
import math
import matplotlib.pyplot as plt
image = cv.imread('images/rice.png', cv.IMREAD_GRAYSCALE)
image=cv.bilateralFilter(image,9,7,7)
thr = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 61, 1)
kernel = np.ones((3,3), np.uint8)
imgEro = cv.erode(thr, kernel, iterations=1)
imgDil = cv.dilate(imgEro, kernel, iterations=1)
obj, labels = cv.connectedComponents(imgDil)
rice_count=obj-1 #remove background
#give different colors to each object
hue=np.uint8(150*labels/np.max(labels))
blank=255*np.ones_like(hue)
labeled=cv.merge([hue,blank,blank])
labeled=cv.cvtColor(labeled,cv.COLOR_HSV2BGR)
labeled[hue==0]=0

f, axarr = plt.subplots(2, 2)
axarr[0, 0].imshow(image,cmap='gray')
axarr[0, 0].set_title("Original image")

axarr[0, 1].imshow(thr,cmap='gray')
axarr[0, 1].set_title("after threshold")

axarr[1, 0].imshow(labeled,cmap='gray')
axarr[1, 0].set_title("color map")

axarr[1, 1].imshow(image,cmap='gray')
axarr[1, 1].set_title("Original image")
plt.show()