from PIL import Image, ImageDraw
from colour import Color
import settings as s
import sys
import topng
from progress import ProgressBar

def setpixel(x, y, value):
    img.putpixel((x, y), value)

def heightmap(hm, scale):
    SCALER = scale

    width, height = hm.size

    img = Image.new('I', (width // SCALER, height // SCALER), color='red')

    prog = ProgressBar(height)

    print("\nHeight Map:")

    for y in range(0, height, SCALER):
        prog.show(y)
        for x in range(0, width // 2, SCALER):
            value = hm.getpixel((x, y))
            rightVal = hm.getpixel((x + width // 2, y))
            try:
                img.putpixel((x // SCALER * 2, y // SCALER), value)
                img.putpixel((x // SCALER * 2 + 1, y // SCALER), rightVal)
            except IndexError:
                pass

    return img

if __name__ == '__main__':
    directory = sys.argv[1]

    Image.MAX_IMAGE_PIXELS = 1061683200
    hm = Image.open("heightmap.tif")

    image = heightmap(hm, s.SCALE)
    image.save(directory + "/hm.tif")

    scaledpng = topng.to_png(image)
    scaledpng.save(directory + "/hm.png")
