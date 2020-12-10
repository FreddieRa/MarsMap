import vectormath as vmath
import math
from PIL import Image, ImageDraw

Image.MAX_IMAGE_PIXELS = (1061683200)

SCALE = 10

smoothness = 20

gradient = [
    (0, "#041318"),
    (2, "#07161a"),
    # (2, "#193E45"),
    (9, "#427e82"),
    (10, "#a6553f"),
    (35, "#f2cba5"),
    (50, "#dfdad6")
]
# gradient = [
#     (0, "#502910"),
#     (35, "#e3b88d"),
#     (50, "#dfdad6")
# ]

# sobelScale = -0.000000034
sobelScale = -0.00000005

light = vmath.Vector3(1, 0.2, 0.8).normalize()

ambientPercentage = 0.15
