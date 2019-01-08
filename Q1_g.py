import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
image = cv.imread('images/im05small.png', cv.IMREAD_GRAYSCALE)
kernal = 5
hs = int(kernal / 2)
for x in range(hs, image.shape[0] - hs - 1):
    for y in range(hs, image.shape[1] - hs - 1):
        l = []
        for a in range(x - hs, x + hs + 1):
            for b in range(y - hs, y + hs + 1):
                l.append(image[a, b])
        l.sort()
        image[x, y] = l[int(len(l) / 2)]
f, axarr = plt.subplots(1, 2)

axarr[0].imshow(img, cmap='gray')
axarr[0].set_title("Original image")

axarr[1].imshow(imgfiltered, cmap='gray')
axarr[1].set_title("Blurred image")
plt.show()

