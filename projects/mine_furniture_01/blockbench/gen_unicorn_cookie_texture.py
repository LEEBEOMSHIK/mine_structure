"""Generate the 16x16 inventory icon for mine_structure:unicorn_cookie.

A round pastel-brown cookie with rainbow choc chips, a little unicorn horn on top,
and a sparkle. Output: resource_pack/textures/items/unicorn_cookie.png
"""
import os

from PIL import Image

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "addon", "resource_pack"))
OUT = os.path.join(BASE, "textures", "items", "unicorn_cookie.png")

DOUGH = (214, 162, 104, 255)
DOUGH_HI = (236, 192, 138, 255)
DOUGH_DK = (176, 124, 76, 255)
WHITE = (255, 255, 255, 255)
CHIPS = [
    (255, 120, 150, 255), (255, 186, 100, 255), (255, 232, 120, 255),
    (140, 214, 150, 255), (130, 190, 245, 255), (196, 150, 240, 255),
]
HORN = [(255, 150, 176, 255), (255, 210, 120, 255), (150, 214, 176, 255), (150, 196, 245, 255)]

img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
cx, cy, r = 7.5, 9.5, 5.6
for y in range(16):
    for x in range(16):
        d = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
        if d <= r:
            if d > r - 1:
                img.putpixel((x, y), DOUGH_DK)
            elif (x - cx) < -1.5 and (y - cy) < -1.5:
                img.putpixel((x, y), DOUGH_HI)
            else:
                img.putpixel((x, y), DOUGH)

# rainbow choc chips
chip_spots = [(5, 8), (10, 7), (7, 11), (9, 11), (6, 6), (11, 10)]
for i, (x, y) in enumerate(chip_spots):
    img.putpixel((x, y), CHIPS[i % len(CHIPS)])

# little unicorn horn on top
horn_spots = [(7, 4), (7, 3), (8, 2), (8, 1)]
for i, (x, y) in enumerate(horn_spots):
    img.putpixel((x, y), HORN[i % len(HORN)])

# sparkle
img.putpixel((4, 5), WHITE)
img.putpixel((12, 6), WHITE)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
img.save(OUT)
print("wrote", OUT)
