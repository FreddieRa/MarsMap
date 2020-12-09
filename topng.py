from PIL import Image, ImageDraw
from colour import Color
import sys
from progress import ProgressBar


def setpixel(x, y, value, img):
    MAX = 1385517713
    MIN = -513154762
    grey = int( ((value + (-MIN)) / (MAX + (-MIN))) * 255 )
    color = (grey, grey, grey)
    img.putpixel((x, y), color)

def to_png(tif):
    width, height = tif.size

    img = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))

    prog = ProgressBar(height-1)

    print("\nTo PNG:")
    for y in range(0, height - 1):
        prog.show(y)
        for x in range(0, width - 1):
            value = tif.getpixel((x, y))
            setpixel(x, y, value, img)

    print("\n")
    return img
