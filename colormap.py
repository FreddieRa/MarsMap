from PIL import Image, ImageDraw
from colour import Color
import settings as s
import sys
from progress import ProgressBar

def ctot(c):
    return int(c.red * 255), int(c.green * 255), int(c.blue * 255)

def setpixel(x, y, value, colors, img):
    MAX = 1385517713
    MIN = -563154762
    colorIndex = int( ((value + (-MIN)) / (MAX + (-MIN))) * (len(colors) - 1) )
    try:
        c = colors[colorIndex]
    except IndexError:
        c = Color("#000000")

    color = ctot(c)
    img.putpixel((x, y), color)


def colormap(hm, gradient, smoothness):
    width, height = hm.size

    img = Image.new('RGBA', (width, height), color=(0, 0, 0, 0))

    colorlist = []

    for g in range(len(gradient) - 1):
        (start, color) = gradient[g]
        (nextStart, nextColor) = gradient[g+1]

        begin = start * smoothness
        end = (nextStart - start) * smoothness

        sublist = list(Color(color).range_to(Color(nextColor), end))
        colorlist += sublist

    prog = ProgressBar(height)

    print("\nColor Map:")

    for y in range(0, height):
        prog.show(y)
        for x in range(0, width):
            value = hm.getpixel((x, y))
            if value != -2147483648:
                setpixel(x, y, value, colorlist, img)
    return img


if __name__ == '__main__':
    directory = sys.argv[1]
    hm = Image.open(directory + "/pm.tif")

    image = colormap(hm, s.gradient, s.smoothness)
    image.save(directory + "/cm.png")
