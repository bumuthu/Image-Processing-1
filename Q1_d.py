import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('images/im05.png', cv.IMREAD_COLOR)
img1 = cv.cvtColor(img, cv.COLOR_RGB2BGR)
f, axarr = plt.subplots(2, 2)

axarr[0, 0].imshow(img1, cmap='gray')
axarr[0, 0].set_title("Original image")

gamma = 0.5
table = np.array([(i/255.0)**(1/gamma)*255.0 for i in (np.arange(0, 256))]).astype('uint8')
axarr[0, 1].imshow(cv.LUT(img1, table), cmap='gray')
axarr[0, 1].set_title("Gamma correction (r = 0.5)")

gamma = 1.5
table = np.array([(i/255.0)**(1/gamma)*255.0 for i in (np.arange(0, 256))]).astype('uint8')
axarr[1, 0].imshow(cv.LUT(img1, table), cmap='gray')
axarr[1, 0].set_title("Gamma correction (r = 1.5)")

gamma = 2.5
table = np.array([(i/255.0)**(1/gamma)*255.0 for i in (np.arange(0, 256))]).astype('uint8')
axarr[1, 1].imshow(cv.LUT(img1, table), cmap='gray')
axarr[1, 1].set_title("Gamma correction (r = 2.5)")

plt.show()
