"""Generate 16x16 textures for the unicorn building blocks.

Outputs to resource_pack/textures/blocks/:
  unicorn_cloud.png, unicorn_candy.png, unicorn_star.png
"""
import os
import random

from PIL import Image

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "addon", "resource_pack"))
BLOCKS = os.path.join(BASE, "textures", "blocks")


def save(img, name):
    os.makedirs(BLOCKS, exist_ok=True)
    img.save(os.path.join(BLOCKS, name))
    print("wrote", os.path.join(BLOCKS, name))


def cloud():
    rng = random.Random(11)
    img = Image.new("RGBA", (16, 16), (244, 248, 255, 255))
    for _ in range(26):
        x, y = rng.randint(0, 15), rng.randint(0, 15)
        img.putpixel((x, y), (220, 232, 248, 255))
    for _ in range(14):
        x, y = rng.randint(0, 15), rng.randint(0, 15)
        img.putpixel((x, y), (255, 255, 255, 255))
    save(img, "unicorn_cloud.png")


def candy():
    img = Image.new("RGBA", (16, 16), (255, 255, 255, 255))
    pink = (246, 150, 196, 255)
    for y in range(16):
        for x in range(16):
            if ((x + y) // 3) % 2 == 0:
                img.putpixel((x, y), pink)
    rng = random.Random(12)
    for _ in range(8):
        img.putpixel((rng.randint(0, 15), rng.randint(0, 15)), (255, 232, 120, 255))
    save(img, "unicorn_candy.png")


def star():
    rng = random.Random(13)
    img = Image.new("RGBA", (16, 16), (60, 52, 104, 255))
    for y in range(16):
        for x in range(16):
            if (x + y) % 7 == 0:
                img.putpixel((x, y), (78, 68, 128, 255))
    for _ in range(7):
        x, y = rng.randint(1, 14), rng.randint(1, 14)
        col = (255, 232, 120, 255)
        img.putpixel((x, y), col)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if 0 <= x + dx < 16 and 0 <= y + dy < 16:
                img.putpixel((x + dx, y + dy), (255, 246, 190, 255))
    save(img, "unicorn_star.png")


def main():
    cloud()
    candy()
    star()


if __name__ == "__main__":
    main()
