import cv2
import numpy as np

def to_gray_scale():
    for i in range(height):
        for j in range(width):
            R, G, B = img[i][j]
            #gs_value = (int(R) + int(G) + int(b)) / 3 
            gs_value = (int(min(R, G, B)) + int(max(R, G, B))) / 2 #gray-scale value
            img[i][j] = [gs_value, gs_value, gs_value]

def show_images():
    cv2.imshow('image', img)
    cv2.imshow('convoluted image', conv_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def convolute():
    #yes, I know it is verry brute forced and totally not efficient on this state, or any state
    for i in range(1, height-1):
        for j in range(1, width-1):
            red = green = blue = 0
            for ii in range(3):
                for jj in range(3):
                    current_pixel = img[i+ii-1][j+jj-1]
                    current_kernel = kernel[ii][jj]

                    red += current_pixel[0] * current_kernel
                    green += current_pixel[1] * current_kernel
                    blue += current_pixel[2] * current_kernel
            
            red /= kernel[3][0]
            green /= kernel[3][0]
            blue /= kernel[3][0]
            
            conv_img[i][j] = [red, green, blue]
    #also I will take care of the borders and corners another day, not the most important for now I think


#reading image obv
img = cv2.imread("download.jpg")
height, width, channels = img.shape

#reading kernel from file
kernel = np.loadtxt("kernel.txt")

#initializing new convoluted picture
conv_img = np.zeros((height, width, channels))

if kernel[3][1] == 1:
    to_gray_scale()

convolute()
#show_images()

cv2.imwrite("convoluted_image.png", conv_img)