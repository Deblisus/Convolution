from PIL import Image

filename = "da.png"

img = Image.open(filename)

for i in range(img.width):
    for j in range(img.height):
        print(img.getpixel((j, i)), end=" ")
    print()

print()
print(img.getpixel((0, 1)))
print(img.getpixel((1, 0)))