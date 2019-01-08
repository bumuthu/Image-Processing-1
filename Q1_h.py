import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image=cv.imread('images/im09small.png',cv.IMREAD_GRAYSCALE)
planes=cv.split(image)
def gaussian_filter(shape, sigma):
    x=shape//2
    y=x
    grid = np.array([[((i**2+j**2)/(2.0*sigma**2)) for i in range(-x, x+1)] for j in range(-y, y+1)])
    g_filter = np.exp(-grid)/(2*np.pi*sigma**2)
    g_filter /= np.sum(g_filter)
    return g_filter
def BilateralFilter(image,sigma1,sigma2,size):
    mid=size//2
    kernelSpace=gaussian_filter(size,sigma1)
    FilteredImage=np.zeros((len(image),len(image[0])))
    for i in range(mid,len(image)-mid-1):
        for j in range(mid,len(image[i])-mid-1):
            kernelCol=np.zeros((size,size))
            kernelCol=np.abs(image[i][j]-image[i-mid:i+mid+1,j-mid:j+mid+1])
            kernelCol=np.exp(-(np.square(kernelCol)/(2*sigma2**2)))
            bil_kernel=np.multiply(kernelSpace,kernelCol)
            FilteredImage[i][j]=(np.sum(np.multiply(bil_kernel,image[i-mid:i+mid+1,j-mid:j+mid+1])))/np.sum(bil_kernel)
    return FilteredImage.astype('uint8')
f, axarr = plt.subplots(2)
axarr[0].imshow(cv.cvtColor(image,cv.COLOR_RGB2BGR))
axarr[0].set_title("Original image")
axarr[1].imshow(cv.cvtColor(newimage,cv.COLOR_RGB2BGR))
axarr[1].set_title("Blurred image")
plt.show()