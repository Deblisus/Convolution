import cv2
import numpy as np

#Should probably make all of this into a class but idk
'''
Brief explanation:
    Trying to make a convolution algorithm from scratch
    not getting way to complicated or something

    functions:
        to_gray_scale: Basically the title, takes the image and converts it to grayscale
                        for example for the edge detection kernels
        convolute: Again, basically the title, takes the selected image and applies the
                        kernel on it (kinda brute forcing)
    
    kernel: 
        Using a 3x3 kernel, the first 3 lines
        The 4th line is some parameters:
            1st number: the number to be divided by to keep the luminance 'accurate' (probably will 'automate'
                            it by summing the values in the kernel and avoiding zero)
            2nd number: 1 or 0, to be converted to gray scale or not to be converted to gray scale
            3rd number: size of kernel. I don't even know how I made it to work but it does WOO!
                        Example: if the kernel is 5x5, the number will be 5
            
'''

'''
    Update!
    Tried to run it with a higher res picture which is not even a huge res one: 1800x525
    It took about 4:45 to run with a sharpening kernel (like it even matters)...
    Yeah, I expected it to be bad, but not really this bad
'''

def to_gray_scale():
    for i in range(height):
        for j in range(width):
            R, G, B = img[i][j]
            #gs_value = (int(R) + int(G) + int(b)) / 3 
            gs_value = (int(min(R, G, B)) + int(max(R, G, B))) / 2 #gray-scale value
            img[i][j] = [gs_value, gs_value, gs_value]
            # I know that I can save about 3 times the memory by ghanging from rgb,
            # but it will not work well with the convolution function, but
            # I probaably will fix that in the future i guess and until then 
            # it will work just fine

def show_images():
    cv2.imshow('image', img)
    cv2.imshow('convoluted image', conv_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def convolute():
    #yes, I know it is verry brute forced and totally not efficient on this state, or any state
    spacer = int(kernel[-1][2]/2)
    
    for i in range(spacer, height-spacer):
        for j in range(spacer, width-spacer):
            red = green = blue = 0
            for ii in range(int(kernel[-1][2])):
                for jj in range(int(kernel[-1][2])):
                    current_pixel = img[i+ii-spacer][j+jj-spacer]
                    current_kernel = kernel[ii][jj]

                    red += current_pixel[0] * current_kernel
                    green += current_pixel[1] * current_kernel
                    blue += current_pixel[2] * current_kernel
            
            red /= kernel[-1][0]
            green /= kernel[-1][0]
            blue /= kernel[-1][0]
            
            conv_img[i][j] = [red, green, blue]
    #also I will take care of the borders and corners another day, not the most important functionality for now I think


    #reading image obv
img = cv2.imread("img.jpg")
height, width, channels = img.shape

#reading kernel from file
kernel = np.loadtxt("kernel.txt")

#initializing new convoluted picture
conv_img = np.zeros((height, width, channels))

#converting to gray scale
if kernel[-1][1] == 1:
    to_gray_scale()

convolute()
#show_images()

#saving the image (why did I type this?)
cv2.imwrite("convoluted_image.png", conv_img)

#main()

def cv2_gaussian():
    img = cv2.imread("img.jpg")

    conv_img = cv2.GaussianBlur(img, (3, 3), 0)

    cv2.imwrite("convoluted_img_cv2.png", conv_img)

#cv2_gaussian()