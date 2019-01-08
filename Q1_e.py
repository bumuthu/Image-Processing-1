import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img1= cv.imread('images/lenna.png', cv.IMREAD_COLOR)

img = cv.cvtColor(img1,cv.COLOR_RGB2BGR)

f, axarr = plt.subplots(1, 2)

axarr[0].imshow(img, cmap='gray')
axarr[0].set_title("Original image")

kernal = np.ones((3, 3), dtype='float32')/9
imgk = cv.GaussianBlur(img, (3, 3), 0)

axarr[1].imshow(imgk, cmap='gray')
axarr[1].set_title('Filtered image 1')

plt.show()
