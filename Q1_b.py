import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('images/lenna.png', cv.IMREAD_GRAYSCALE)

img1 = cv.cvtColor(img, cv.COLOR_GRAY2RGB)

f, axarr = plt.subplots(2, 2)

axarr[0, 0].imshow(img, cmap='gray')
axarr[0, 0].set_title("Original image")

axarr[0, 1].hist(img.ravel(), 256, [0, 256], color='r')
axarr[0, 1].set_title("Histogram")

eq = cv.equalizeHist(img)
axarr[1, 0].imshow(eq, cmap='gray')
axarr[1, 0].set_title("Equalized image")

axarr[1, 1].hist(eq.ravel(), 256, [0, 256], color='b')
axarr[1, 1].set_title("Equalized histogram")
print(type(img))

print(np.array([(54,6),(77,32)]))
a = np.array([(54,6),(256,32)]).astype('uint8')
print(a)

plt.show()




def imageShow(img):
    plt.imshow(img)
    plt.title('Image')
    plt.show()