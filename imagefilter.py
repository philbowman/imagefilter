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
    image = Image.open('jump.jpeg')

    # Show image
    image.show()

    # get the height and width
    width, height = image.size

    # get the rgb values of a pixel at a certain coordinate
    r, g, b = image.getpixel((50, 50))
    
    # create a new image of the same size as the original
    new_image = Image.new("RGB", (image.size), "white")

    # place a pixel from the original image into the new image
    new_image.putpixel((50, 50), (r, g, b))


    # Save the image
    new_image.save(IMAGENAME + "_modified." + EXTENSION)

    # open the new image
    # new_image.show()

if __name__ == "__main__":
    main()