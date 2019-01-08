import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
image = cv.imread('images/im02.png', cv.IMREAD_COLOR)
red, green, blue = cv.split(image)  # splitting image in to three
red2 = np.reshape(red, (1, np.product(red.shape)))[0]
green2 = np.reshape(green, (1, np.product(green.shape)))[0]  # making 1D array of the image
blue2 = np.reshape(blue, (1, np.product(blue.shape)))[0]
imagemap = [red2, green2, blue2]
mn = image.shape[0] * image.shape[1]
for count in range(0, 3):
    unique, nk = np.unique(imagemap[count], return_counts=True)
    prnk = nk / mn
    newvalue = np.zeros(256)
    cumvalue = 0
    for i, x in enumerate(prnk):
        cumvalue += x
        newvalue[i] = 255 * cumvalue
    for x in range(0, image.shape[0]):
        for y in range(0, image.shape[1]):
            pval = image[:, :, count][x, y]
            image[:, :, count][x, y] = newvalue[pval]
color = ("r", "g", "b")
for e, c in enumerate(color):
    hist = cv.calcHist([image[:, :, e]], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)
plt.show()


