import cv2
import numpy as np
import time
#import concurrent.futures
#import multiprocessing
import threading

start_time = time.time()

#Should probably make all of this into a class but idk
'''
Brief explanation:
    Trying to make a convolution algorithm from scratch
    not getting way to complicated or something

    functions:
        to_gray_scale: Basically the title, takes the image and converts it to grayscale
                        for example for the edge detection kernels
        convolute: Again, basically the title, takes the selected image and applies the
                        kernel on it
        calc_divider: Automatically calculates the dividing factor during the convolution
                        For example if the kernel is 3x3 and composed only of ones, normally
                        the kernel actually consists of 1/9s for the luminosity to remain
                        constant. I made the function that sums the elements of kernel
                        and returns it, if the number is 0, it returns 1 because dividing by 0
    
    kernel: 
        Using a 3x3 kernel, the first 3 lines
        The 4th line is some parameters:
            1st number: the number to be divided by to keep the luminance 'accurate' (probably will 'automate'
                            it by summing the values in the kernel and avoiding zero)
            2nd number: 1 or 0, to be converted to gray scale or not to be converted to gray scale
            3rd number: size of kernel. I don't even know how I made it to work but it does WOO!
                        Example: if the kernel is 5x5, the number will be 5
            
'''




def threading_convolute(start_pos, end_pos, index):
    #yes, I know it is verry brute forced and totally not efficient on this state, or any state
    spacer = int(kernel[-1][2]/2)
    size = int(kernel[-1][2])
    #print(start_pos)

    actual_kernel = kernel[0:size]
    #print(end_pos+spacer, height-spacer)
    print(index)

    divider = calc_divider(actual_kernel)
    for i in range(start_pos+spacer, end_pos+spacer):
        for j in range(spacer, width-spacer):
            # This ain't pretty, but definately much faster. Finally implemented matrix multiplication

            curr_bgr_section = img[i-spacer:i+spacer+1, j-spacer:j+spacer+1]
            
            blue_section = curr_bgr_section[0:size, 0:size, 0]
            green_section = curr_bgr_section[0:size, 0:size, 1]
            red_section = curr_bgr_section[0:size, 0:size, 2]

            blue = ((blue_section * actual_kernel) / divider).sum()
            green = ((green_section * actual_kernel) / divider).sum()
            red = ((red_section * actual_kernel) / divider).sum()
            
            conv_img[i][j] = [blue, green, red]
    #also I will take care of the borders and corners another day, not the most important functionality for now I think

    
def threadng(threads):
    if threads == 0:
        threads = 1
    
    dist = int(height / threads)
    times = list(range(0, height, dist))
    times.pop()
    print(times)
    print(dist)

    #with concurrent.futures.ThreadPoolExecutor() as executor:
        #process = executor.map(threading_convolute, times)
        #process = [executor.submit(threading_convolute, pos, dist) for pos in times]
    processes = []
    for strt in times:
        t = threading.Thread(target=threading_convolute, args=(strt, strt+dist, strt//dist))
        t.start()
        processes.append(t)
    
    for t in processes:
        t.join()



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


def calc_divider(kernel):
    div = kernel.sum()
    
    if div:
        return div
    return 1



def convolute():
    #yes, I know it is verry brute forced and totally not efficient on this state, or any state
    spacer = int(kernel[-1][2]/2)
    size = int(kernel[-1][2])

    actual_kernel = kernel[0:size]

    divider = calc_divider(actual_kernel)
    
    for i in range(spacer, height-spacer):
        for j in range(spacer, width-spacer):
            # This ain't pretty, but definately much faster. Finally implemented matrix multiplication
            
            curr_bgr_section = img[i-spacer:i+spacer+1, j-spacer:j+spacer+1]
            
            blue_section = curr_bgr_section[0:size, 0:size, 0]
            green_section = curr_bgr_section[0:size, 0:size, 1]
            red_section = curr_bgr_section[0:size, 0:size, 2]

            blue = ((blue_section * actual_kernel) / divider).sum()
            green = ((green_section * actual_kernel) / divider).sum()
            red = ((red_section * actual_kernel) / divider).sum()
            
            conv_img[i][j] = [blue, green, red]
    #also I will take care of the borders and corners another day, not the most important functionality for now I think
    


#reading image obv
img = cv2.imread("pic.jpg")
height, width, channels = img.shape

kernel = np.loadtxt("kernel.txt")

#initializing new convoluted picture
conv_img = np.zeros((height, width, channels))

#converting to gray scale
if kernel[-1][1] == 1:
    to_gray_scale()

#threadng(kernel[-1][0])
convolute()
#show_images()

conv_img = conv_img[1:height-1, 1:width-1]


#saving the image (why did I type this?)
cv2.imwrite("convoluted_image2.png", conv_img)



def cv2_gaussian():
    img = cv2.imread("picture.jpg")

    conv_img = cv2.GaussianBlur(img, (7, 7), 0)

    cv2.imwrite("convoluted_image2.png", conv_img)

#cv2_gaussian()

print(round(time.time() - start_time, 2), "seconds")