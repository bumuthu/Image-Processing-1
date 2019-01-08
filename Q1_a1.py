import cv2 as cv
from matplotlib import pyplot as plt
def histogram(img):
    global j
    global m
    global n
    j += 1
    print(j)
    colors = ['r','g','b']
    histList = []
    for i in range(256):
        histList.append((img.ravel().tolist().count(i)))
    axarr[1].plot(histList, color=colors[j-1])
    axarr[1].set_title('Histogram')
j = 0
img = cv.imread('images/im05.png', cv.IMREAD_COLOR)
red, green, blue =cv.split(img)
img = cv.cvtColor(img,cv.COLOR_RGB2BGR)
m = img.shape[0]
n = img.shape[1]
f, axarr = plt.subplots(1, 2)
axarr[0].imshow(img)
axarr[0].set_title("Original image")
histogram(red)
histogram(green)
histogram(blue)
plt.show()
