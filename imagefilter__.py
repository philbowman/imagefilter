# run pip install pillow to install
from PIL import Image
import math

def main():
    # Open image
    image = Image.open('jump.jpeg')

    # Show image
    # image.show()

    # get the height and width
    width, height = image.size

    # get the rgb values of a pixel at a certain coordinate
    r, g, b = image.getpixel((50, 50))
    
    # create a new image of the same size as the original
    new_image = Image.new("RGB", (image.size), "white")

    # place a pixel from the original image into the new image
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            new_image.putpixel((x, y), (math.floor(r/2), math.floor(g/2), math.floor(b/2)))

    image = Image.open('jump.jpeg')
    new_image1 = grayscale(image, True)
    new_image2 = grayscale(image, False)
    # open the new image
    new_image.show()

def grayscale(image, alt_formula):
    new_image = None
    #convert each pixel to grayscale
    # iterate over each pixel in the original
        # for each pixel:
            # if using formula 1:
            if alt_formula:
                # for each pixel, convert it to gray using f1
            else:
                # use f2


    return new_image

if __name__ == "__main__":
    main()