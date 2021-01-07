# Convolution from scratch
 Trying to build a convolution program from scratch. Gave up on c++ so python it is

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
            3rd number: TBD, maybe for the edge detection to apply both sides
                            (left oriented and right oriented edge detection kernel) to the image