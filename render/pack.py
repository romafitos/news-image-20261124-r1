"""Packs the raw screenshot into the entry PNG and prints the page's vital signs.

usage: python3 pack.py raw.png entry.png
Tries a fixed ladder of encodings (palette, then posterised RGB) and keeps the
first that lands in the 175-200 KB band, else the one nearest to it. The ladder
is fixed, so the same raw shot always gives the same bytes.
Reports: bytes, dark-ink share (luma < 96), red share; writes a 300 px thumbnail.
"""
import io
import sys

from PIL import Image, ImageOps

LO, HI = 180_000, 230_000


def measure(img):
    rgb = img.convert("RGB")
    n = rgb.width * rgb.height
    dark = red = 0
    for r, g, b in rgb.getdata():
        if 0.299 * r + 0.587 * g + 0.114 * b < 96:
            dark += 1
        if r > 150 and g < 80 and b < 90:
            red += 1
    return dark / n, red / n


def encode(img):
    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    return buf.getvalue()


def ladder(raw):
    # richest palette first, so the page keeps its colours whenever the size band allows; octree keeps the
    # flat brand colours (continent pins, tag badges) exact where median-cut drifted them
    for colors in (256, 192, 160, 128, 96, 80, 64):
        yield f"palette{colors}", raw.quantize(colors=colors, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE)
    for bits in (4, 5, 6):
        yield f"posterize{bits}", ImageOps.posterize(raw, bits)


def main():
    src, dst = sys.argv[1], sys.argv[2]
    raw = Image.open(src).convert("RGB")
    assert raw.size == (1024, 1024), raw.size
    best = None
    for name, img in ladder(raw):
        data = encode(img)
        gap = 0 if LO <= len(data) <= HI else min(abs(len(data) - LO), abs(len(data) - HI))
        print(f"  try {name:<11} {len(data):>7} B")
        if best is None or gap < best[0]:
            best = (gap, name, data)
        if gap == 0:
            break
    _, name, data = best
    with open(dst, "wb") as f:
        f.write(data)
    out = Image.open(dst)
    ink, red = measure(out)
    out.convert("RGB").resize((300, 300), Image.LANCZOS).save("/tmp/ni24-thumb300.png")
    print(f"chose {name}: bytes {len(data)}  ink {ink*100:.1f}%  red {red*100:.2f}%  thumb /tmp/ni24-thumb300.png")


if __name__ == "__main__":
    main()
