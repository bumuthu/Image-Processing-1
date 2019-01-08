import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/im09small.png', cv.IMREAD_GRAYSCALE)

imgfiltered = cv.bilateralFilter(img, 10, 50, 50)

f, axarr = plt.subplots(2)

axarr[0].imshow(img, cmap='gray')
axarr[0].set_title("Original image")

axarr[1].imshow(imgfiltered, cmap='gray')
axarr[1].set_title("Blurred image")
plt.show()

