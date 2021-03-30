# Convolution from scratch
 Trying to build a convolution program from scratch. Gave up on c++ so python it is
 
## Multithreading is on the way

Brief explanation:
    Trying to make a convolution algorithm from scratch
    not getting way too complicated or something

    functions:
        to_gray_scale: Basically the title, takes the image and converts it to grayscale
                        for example for the edge detection kernels
        convolute: Again, basically the title, takes the selected image and applies the
                        kernel on it (kinda brute forcing)
        calc_divider: Automatically calculates the dividing factor during the convolution
                        For example if the kernel is 3x3 and composed only of ones, normally
                        the kernel actually consists of 1/9s for the luminosity to remain
                        constant. I made the function that sums the elements of kernel
                        and returns it, if the number is 0, it returns 1 because dividing by 0
    
    kernel: 
        Using a 3x3 kernel, the first 3 lines
        The 4th line is some parameters:
            1st number: Number of threads to be used for processing. Can't get it to work just yet
            2nd number: 1 or 0, to be converted to gray scale or not to be converted to gray scale
            3rd number: size of kernel. I don't even know how I made it to work but it does WOO!
                        Example: if the kernel is 5x5, the number will be 5
