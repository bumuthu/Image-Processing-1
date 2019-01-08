import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("images/im06small.png", cv.IMREAD_GRAYSCALE)
factor = 4
n = img.shape[1]
m = img.shape[0]

newImg = np.zeros((m * factor, n * factor))
for y in range(0, m):
    for x in range(0, n):
        newImg[y * factor, x * factor] = img[y, x]
for y in range(0, m * factor, factor):
    for x in range(0, (n - 1) * factor, factor):

        for a in range(x + 1, x + factor):
            newImg[y, a] = int(newImg[y, x] + (newImg[y, x + factor] - newImg[y, x]) / factor * (a - x))
for x in range(0, n * factor):
    for y in range(0, (m - 1) * factor, factor):
        for a in range(y + 1, y + factor):
            newImg[a, x] = int(newImg[y, x] + (newImg[y + factor, x] - newImg[y, x]) / factor * (a - y))

f, axarr = plt.subplots(2)

axarr[0].imshow(img, cmap='gray')
axarr[0].set_title("Original image")

axarr[1].imshow(newImg, cmap='gray')
axarr[1].set_title("Bilinear Zoomed image")

plt.show()