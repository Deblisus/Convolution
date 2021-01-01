from PIL import Image

def print_img(image):
    for i in range(image.width):
        for j in range(image.height):
            print(image.getpixel((j, i)), end=" ")
        print()

filename = "download.jpg"

img = Image.open(filename)
#print_img(img)
print()
print(img.mode)

img.convert(mode="L")
img.save("pic.jpg")