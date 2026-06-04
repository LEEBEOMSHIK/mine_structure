"""Generate 16x16 inventory icons for the unicorn food/treat items and the wand.

Outputs to resource_pack/textures/items/:
  unicorn_cupcake.png, unicorn_lollipop.png, unicorn_rainbow_drink.png,
  unicorn_star_candy.png, unicorn_wand.png
"""
import os

from PIL import Image

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "addon", "resource_pack"))
ITEMS = os.path.join(BASE, "textures", "items")
CLEAR = (0, 0, 0, 0)
WHITE = (255, 255, 255, 255)
RAINBOW = [
    (255, 120, 150, 255), (255, 186, 100, 255), (255, 232, 120, 255),
    (140, 214, 150, 255), (130, 190, 245, 255), (196, 150, 240, 255),
]


def new():
    return Image.new("RGBA", (16, 16), CLEAR)


def save(img, name):
    os.makedirs(ITEMS, exist_ok=True)
    img.save(os.path.join(ITEMS, name))
    print("wrote", os.path.join(ITEMS, name))


def rect(img, x0, y0, x1, y1, c):
    for y in range(y0, y1):
        for x in range(x0, x1):
            if 0 <= x < 16 and 0 <= y < 16:
                img.putpixel((x, y), c)


def cupcake():
    img = new()
    # wrapper (pink trapezoid)
    for i, y in enumerate(range(9, 15)):
        rect(img, 4 + i // 2, y, 12 - i // 2, y + 1, (244, 150, 196, 255))
    for x in range(5, 11):
        if (x % 2) == 0:
            rect(img, x, 9, x + 1, 15, (224, 120, 172, 255))
    # frosting swirl (white with rainbow sprinkles)
    rect(img, 4, 6, 12, 9, (255, 250, 250, 255))
    rect(img, 5, 4, 11, 6, (255, 250, 250, 255))
    rect(img, 6, 3, 10, 4, (255, 250, 250, 255))
    for (x, y), c in zip([(5, 7), (9, 7), (7, 5), (6, 4), (10, 6)], RAINBOW):
        img.putpixel((x, y), c)
    img.putpixel((8, 2), (228, 72, 86, 255))  # cherry
    save(img, "unicorn_cupcake.png")


def lollipop():
    img = new()
    # stick
    rect(img, 8, 9, 9, 15, (236, 232, 224, 255))
    # round candy with rainbow swirl
    cx, cy, r = 7.5, 5.5, 4.2
    for y in range(16):
        for x in range(16):
            d = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            if d <= r:
                band = int((x + y)) % len(RAINBOW)
                img.putpixel((x, y), RAINBOW[band])
    img.putpixel((6, 4), WHITE)
    save(img, "unicorn_lollipop.png")


def rainbow_drink():
    img = new()
    # cup
    rect(img, 5, 5, 11, 15, (236, 240, 248, 255))
    rect(img, 5, 5, 11, 6, (210, 220, 235, 255))
    # rainbow liquid layers
    layers = [(7, (196, 150, 240, 255)), (8, (130, 190, 245, 255)), (9, (140, 214, 150, 255)),
              (10, (255, 232, 120, 255)), (11, (255, 186, 100, 255)), (12, (255, 120, 150, 255))]
    for y, c in layers:
        rect(img, 6, y, 10, y + 1, c)
    # straw
    rect(img, 9, 2, 10, 7, (255, 120, 150, 255))
    img.putpixel((6, 6), WHITE)
    save(img, "unicorn_rainbow_drink.png")


def star_candy():
    img = new()
    star = (255, 226, 110, 255)
    edge = (240, 196, 70, 255)
    pts = [
        (7, 1), (8, 1),
        (7, 2), (8, 2),
        (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3),
        (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4),
        (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5),
        (6, 6), (7, 6), (8, 6), (9, 6),
        (5, 7), (6, 7), (9, 7), (10, 7),
        (4, 8), (5, 8), (10, 8), (11, 8),
    ]
    for x, y in pts:
        img.putpixel((x, y), star)
    img.putpixel((6, 4), WHITE)
    img.putpixel((9, 5), edge)
    save(img, "unicorn_star_candy.png")


def wand():
    img = new()
    # diagonal handle (gold)
    for i in range(7):
        x, y = 4 + i, 14 - i
        img.putpixel((x, y), (214, 170, 96, 255))
        if x + 1 < 16:
            img.putpixel((x + 1, y), (176, 132, 70, 255))
    # star topper (rainbow) near top-right
    star = [(10, 3), (11, 2), (12, 3), (9, 4), (13, 4), (10, 5), (12, 5), (11, 6), (11, 4)]
    for i, (x, y) in enumerate(star):
        img.putpixel((x, y), RAINBOW[i % len(RAINBOW)])
    img.putpixel((11, 1), WHITE)
    save(img, "unicorn_wand.png")


def main():
    cupcake()
    lollipop()
    rainbow_drink()
    star_candy()
    wand()


if __name__ == "__main__":
    main()
