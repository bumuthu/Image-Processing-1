import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import math
def gaussianKernel(size, sigma):
    gaussKernel = np.zeros((size, size), dtype=np.float32)
    for i in range(0, size):
        for j in range(0, size):
            x = i - (math.floor(size / 2))
            y = j - (math.floor(size / 2))
            gaussKernel[i][j] = (1 / (2 * math.pi * (sigma ** 2))) * math.exp((-1 / (2 * math.pi * (sigma ** 2))) * ((x ** 2) + (y ** 2)))
    return gaussKernel
def filter(image, kernel):
    assert kernel.shape[0] % 2 == 1 and kernel.shape[1] % 2 == 1
    k_hh, k_hw = math.floor(kernel.shape[0] / 2), math.floor(kernel.shape[1] / 2)
    h, w = image.shape
    image_float = cv.normalize(image.astype('float'), None, 0.0, 1.0, cv.NORM_MINMAX)
    result = np.zeros(image.shape, 'float')
    for i in range(k_hh, h - k_hh):
        for j in range(k_hw, w - k_hw):
            result[i, j] = np.dot(image_float[i - k_hh: i + k_hh + 1, j - k_hw: j + k_hw + 1].flatten(),
                                  kernel.flatten())
    result = cv.normalize(result.astype('float'), None, 0.0, 1.0, cv.NORM_MINMAX)
    result = result * 255.0
    return result.astype(np.uint8)
img = cv.imread('images/im05small.png', cv.IMREAD_COLOR)
blue, red, green = cv.split(img)
kernel = gaussianKernel(5, 1)
imgb = filter(blue, kernel)
imgr = filter(red,kernel)
imgg = filter(green,kernel)
filtered_img = cv.merge((imgb, imgr, imgg))
f, axarr = plt.subplots(2)
axarr[0].imshow(cv.cvtColor(img,cv.COLOR_RGB2BGR))
axarr[0].set_title("Original image")
axarr[1].imshow(cv.cvtColor(filtered_img,cv.COLOR_RGB2BGR))
axarr[1].set_title("Blurred image")
plt.show()


