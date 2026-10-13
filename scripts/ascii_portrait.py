#!/usr/bin/env python3
"""One-off: turn a portrait photo into ASCII art for the profile card.

Needs Pillow. Run locally; the output text file is committed, the photo is not.

    python3 scripts/ascii_portrait.py PHOTO > card/portrait.txt

The backdrop is removed by flood-filling from the image border, so dark hair and
clothing keep a faint texture and the silhouette survives on a dark card.
"""
import sys
from collections import deque

from PIL import Image, ImageFilter

COLS, ROWS = 54, 28
CROP = (140, 0, 500, 372)     # left, top, right, bottom in source pixels
SCALE = 4                     # working pixels per character cell, horizontally
STEP_TOL = 3                  # max brightness step between neighbours inside the backdrop
BACKDROP = (18, 75)           # brightness band the backdrop lives in
SKIN_FLOOR = 70               # below this, a subject pixel is hair / clothing / shadow
DARK = ":"                    # texture for dark parts of the subject
RAMP = "-=+*cox#%@"           # skin, dark -> bright


def backdrop_mask(px, w, h):
    seen = [[False] * w for _ in range(h)]
    queue = deque()
    for x in range(w):
        queue += [(x, 0), (x, h - 1)]
    for y in range(h):
        queue += [(0, y), (w - 1, y)]
    while queue:
        x, y = queue.popleft()
        if seen[y][x] or not BACKDROP[0] <= px[x, y] <= BACKDROP[1]:
            continue
        seen[y][x] = True
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and not seen[ny][nx] and abs(px[nx, ny] - px[x, y]) <= STEP_TOL:
                queue.append((nx, ny))
    return seen


def main(path):
    w, h = COLS * SCALE, ROWS * SCALE * 2
    img = Image.open(path).convert("L").crop(CROP).resize((w, h), Image.LANCZOS)
    img = img.filter(ImageFilter.GaussianBlur(0.8))
    px = img.load()
    backdrop = backdrop_mask(px, w, h)
    cw, ch = SCALE, SCALE * 2
    lines = []
    for r in range(ROWS):
        row = ""
        for c in range(COLS):
            cells = [(x, y) for y in range(r * ch, (r + 1) * ch) for x in range(c * cw, (c + 1) * cw)]
            subject = [px[x, y] for x, y in cells if not backdrop[y][x]]
            if len(subject) < len(cells) / 2:
                row += " "
                continue
            v = sum(subject) / len(subject)
            if v < SKIN_FLOOR:
                row += DARK
            else:
                t = min((v - SKIN_FLOOR) / (215 - SKIN_FLOOR), 0.999)
                row += RAMP[int(t * len(RAMP))]
        lines.append(row.rstrip())
    print("\n".join(lines))


if __name__ == "__main__":
    main(sys.argv[1])
