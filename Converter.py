import numpy
from PIL import Image
from requester import catimage_request
import numpy as np
from EdgeDetect import image_edges
ascii_characters_by_surface = "$@B%8&WM#ZO0QLCJUYX/\\{}[]|oahkbdpqwmzcvunxrjft()1?i!lI;:*-_+~,\"^`"

image_with_edges = image_edges()
image = Image.open('cat_with_edges.png')
(width, height) = image.size


def main():
    ascii_art = convert_to_ascii_art(image)
    save_as_text(ascii_art)


def convert_to_ascii_art(image):
    ascii_art = []
    for y in range(0, height - 1, 2):
        line = ''
        for x in range(0, width - 1):
            px = image.getpixel((x, y))
            px2 = image.getpixel((x, y + 1))
            line += convert_pixels_to_character(px, px2)
        ascii_art.append(line)
    return ascii_art


def convert_pixels_to_character(pixel1, pixel2):
    (r, g, b) = pixel1
    (r2, g2, b2) = pixel2
    pixel_brightness = (r + g + b + r2 + g2 + b2) / 2
    max_brightness = 255 * 3
    brightness_weight = len(ascii_characters_by_surface) / max_brightness
    index = int(pixel_brightness * brightness_weight) - 1
    return ascii_characters_by_surface[index]


def save_as_text(ascii_art):
    with open("image.txt", "w") as file:
        for line in ascii_art:
            file.write(line)
            file.write('\n')
        file.close()


if __name__ == '__main__':
    main()
