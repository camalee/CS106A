"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'


def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    for pixel in final_image:
        make_recolored_patch(red_scale, green_scale, blue_scale)

    # This is an example which should generate a pinkish patch
    patch = make_recolored_patch(1.5, 0, 1.5)
    final_image.show()


def make_recolored_patch(red_scale, green_scale, blue_scale):
    """
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    """

    patch = SimpleImage(PATCH_NAME)
    r = pixel.red
    g = pixel.green
    b = pixel.blue
    if red_scale:
        pixel.red = r * 1.5
        pixel.green = 0
        pixel.blue = 0
    if green_scale:
        pixel.red = 0
        pixel.green = g * 1.5
        pixel.blue = 0
    if blue_scale:
        pixel.red = 0
        pixel.green = 0
        pixel.blue = b * 1.5
    return patch


if __name__ == '__main__':
    main()
