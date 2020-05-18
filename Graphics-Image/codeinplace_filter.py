"""
File: codeinplace_filter.py
----------------
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()

    # Apply the filter
    for pixel in image:
        apply_filter(pixel)

    # Show the image after the transform
    image.show()
    
def apply_filter(pixel):
    r = pixel.red
    g = pixel.green
    b = pixel.blue
    pixel.red = r * 1.5
    pixel.green = g * 0.7
    pixel.blue = b * 1.5


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
