import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import math
image = cv.imread('images/im03small.png',cv.IMREAD_GRAYSCALE)
def filter2d(image, kernel):
    assert kernel.shape[0]%2 == 1 and kernel.shape[1]%2 == 1
    k_hh, k_hw = math.floor(kernel.shape[0]/2), math.floor(kernel.shape[1]/2)
    h, w = image.shape
    image_float = cv.normalize(image.astype('float'), None, 0.0, 1.0, cv.NORM_MINMAX)
    result = np.zeros(image.shape, 'float')
    for i in range(k_hh, h - k_hh):
        for j in range(k_hw, w - k_hw):
            result[i,j] = np.dot(image_float[i-k_hh:i + k_hh + 1, j - k_hw : j + k_hw + 1].flatten(), kernel.flatten())
    return result
def gaus(size,sigma):
    shape=(size,size)
    x, y = [edge /2 for edge in shape]
    x=int(x)
    y=int(y)
    grid = np.array([[((i**2+j**2)/(2.0*sigma**2)) for i in range(-x, x+1)] for j in range(-y, y+1)])
    g_filter = np.exp(-grid)/(2*np.pi*sigma**2)
    g_filter /= np.sum(g_filter)
    return g_filter
g_filter=gaus(31,10)
bimage=filter2d(image,g_filter)
image = cv.normalize(image.astype('float'), None, 0.0, 1.0, cv.NORM_MINMAX)
bimage = cv.normalize(bimage.astype('float'), None, 0.0, 1.0, cv.NORM_MINMAX)
image3=image-bimage
image3=image3*255.0
image3.astype(np.uint8)
plt.imshow(image3,cmap="gray")
plt.show()
