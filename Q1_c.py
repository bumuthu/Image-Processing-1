import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img1= cv.imread('images/im03.png', cv.IMREAD_COLOR)
img = cv.cvtColor(img1,cv.COLOR_RGB2BGR)
f, axarr = plt.subplots(2, 2)
axarr[0, 0].imshow(img, cmap='gray')
axarr[0, 0].set_title("Original image")
x = np.arange(0, 256)
axarr[0, 1].plot(x)
y = np.arange(255,-1,-1)
axarr[1, 1].plot(y)
axarr[1, 0].imshow(cv.LUT(img, y),cmap='gray')
axarr[1, 0].set_title("Transformed image")
plt.show()