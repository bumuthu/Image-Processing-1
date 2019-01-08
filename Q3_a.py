import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("images/im06small.png", cv.IMREAD_GRAYSCALE)
print(img.shape)
n = img.shape[0]
m = img.shape[1]
scaleFactor = 4

zeroImg = np.zeros((n*scaleFactor, m*scaleFactor))


for i in range(n):
    for j in range(m):
        for k in range(scaleFactor):
            for l in range(scaleFactor):
                zeroImg[scaleFactor*i+k, scaleFactor*j+l] = img[i, j]

f, axarr = plt.subplots(2)

axarr[0].imshow(img, cmap='gray')
axarr[0].set_title("Original image")

axarr[1].imshow(zeroImg, cmap='gray')
axarr[1].set_title("Zoomed image")

plt.show()
