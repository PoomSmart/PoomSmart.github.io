#!/usr/bin/env python3
"""Generate a 1200x630 OG/social-preview image for PoomSmart's Repository.

Pillow-only, portable (no network, no external assets). Draws a dark-themed
jailbreak-tweak-repository card matching the site's palette (#000 bg, #bbb
text, skyblue accent) with a package-box motif.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (0, 0, 0)
CARD = (17, 17, 17)
TEXT = (187, 187, 187)
TITLE = (255, 255, 255)
ACCENT = (135, 206, 235)  # skyblue
MUTED = (120, 120, 120)

FONT_DIR = "/usr/share/fonts/truetype"
def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

def rounded(draw, box, r, fill):
    draw.rounded_rectangle(box, radius=r, fill=fill)

def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # subtle top accent bar
    d.rectangle([0, 0, W, 8], fill=ACCENT)

    # package-box motif (left)
    bx0, by0, bx1, by1 = 120, 200, 360, 440
    rounded(d, [bx0, by0, bx1, by1], 24, CARD)
    d.rectangle([bx0, by0, bx1, by0 + 8], fill=ACCENT)  # lid accent
    # tape / ribbon
    d.rectangle([bx0 + 40, by0 + 40, bx1 - 40, by0 + 48], fill=ACCENT)
    # "repo" pill
    pill_w = 150
    rounded(d, [bx0 + 60, by1 - 70, bx0 + 60 + pill_w, by1 - 34], 18, (34, 34, 34))
    d.text((bx0 + 60 + 20, by1 - 62), "repo", font=font("dejavu/DejaVuSans-Bold.ttf", 26), fill=ACCENT)

    # title
    d.text((440, 210), "PoomSmart's", font=font("dejavu/DejaVuSans-Bold.ttf", 64), fill=TITLE)
    d.text((440, 290), "Repository", font=font("dejavu/DejaVuSans-Bold.ttf", 64), fill=TITLE)

    # subtitle
    d.text((440, 400), "Add PoomSmart's jailbreak repository to", font=font("dejavu/DejaVuSans.ttf", 30), fill=TEXT)
    d.text((440, 448), "Cydia, Installer, Sileo, or Zebra.", font=font("dejavu/DejaVuSans.ttf", 30), fill=TEXT)

    # footer
    d.text((440, 540), "poomsmart.github.io", font=font("dejavu/DejaVuSans-Bold.ttf", 28), fill=MUTED)

    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "og-image.png")
    img.save(out, "PNG")
    print("wrote", out)

if __name__ == "__main__":
    main()
