import cv2
import numpy as np



def show_images():
    cv2.imshow('image', img)
    cv2.imshow('convoluted image', conv_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def convolute():
    #yes, I know it is verry brute forced and totally not efficient on this state, or any state
    for i in range(1, height-1):
        for j in range(1, width-1):
            sum = 0
            for ii in range(3):
                for jj in range(3):
                    sum += img[i+ii-1][j+jj-1][0] * kernel[ii][jj] # basically assuming the image is B/W
            sum /= 9

            conv_img[i][j] = [sum, sum, sum]
    #also I will take care of the borders and corners another day, not the most important for now I think


#reading image obv
img = cv2.imread("download.jpg")
height, width, channels = img.shape

#reading kernel from file
kernel = np.loadtxt("kernel.txt")

#initializing new convoluted picture
conv_img = np.zeros((height, width, channels))

convolute()
show_images()

cv2.imwrite("da22.png", conv_img)