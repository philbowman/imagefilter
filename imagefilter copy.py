# run pip install pillow to install
from PIL import Image

PATH = 'jump.jpeg'
IMAGENAME = ".".join(PATH.split("/")[-1].split(".")[:-1])
EXTENSION = PATH.split("/")[-1].split(".")[-1]
print(PATH)
print(IMAGENAME)
print(EXTENSION)

def main():
    # Open image
    image = Image.open(PATH)

    # Show image

    # get the height and width
    width, height = image.size
    
    # grayscale_image = grayscale(image)
    
    # grayscale_image.save(IMAGENAME + "_grayscale." + EXTENSION)

    shrunk_image = shrink(image)

    shrunk_image.save(IMAGENAME + "_shrunk." + EXTENSION)


def shrink(image):
    width, height = image.size
    newsize = (int(width/2), int(height/2))
    new_image = Image.new("RGB", (int(width/2), int(height/2)), "white")
    newx = 0
    newy = 0
    for x in range(0, width, 2):
        for y in range(0, height, 2):
            r, g, b = image.getpixel((x, y))
            r2, g2, b2 = image.getpixel((x+1, y))
            r3, g3, b3 = image.getpixel((x+1, y+1))
            r4, g4, b4 = image.getpixel((x, y+1))

            new_r = int((r + r4 + r2 + r3)/4)
            new_g = int((g + g4 + g2 + g3)/4)
            new_b = int((b + b4 + b2 + b3)/4)
            new_image.putpixel((newx, newy), (new_r, new_g, new_b))
            newy += 1
        newy = 0
        newx += 1
    return new_image


def grayscale(image):
    width, height = image.size
    new_image = Image.new("RGB", (image.size), "white")
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            avg = int((r + g + b) / 3)
            new_r = avg
            new_g = avg
            new_b = avg
            new_image.putpixel((x, y), (new_r, new_g, new_b))
    return new_image


if __name__ == "__main__":
    main()