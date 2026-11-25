"""news-image-20261124 entry: writes the day's front page to the output folder.

The picture itself is drawn ahead of time by render/page.py (HTML + inline SVG,
shot to PNG by headless Chromium) and kept in this repository as entry.png.
At grading time there is no network, so this program only has to hand that
exact file over, byte for byte, which keeps both required runs identical.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


MAX_BYTES = 1024 * 1024  # contest limit: one image, at most 1 MiB
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def output_dir() -> str:
    # The grader mounts /output; MAKEFUN_OUTPUT_DIR lets a local run point elsewhere.
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_source() -> None:
    # Fail loudly rather than hand over a missing, oversized or non-PNG file.
    if not os.path.isfile(SOURCE):
        raise SystemExit("entry.png is missing; run render/page.py and render/shoot.sh first")
    size = os.path.getsize(SOURCE)
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png is {size} bytes, over the 1 MiB limit")
    with open(SOURCE, "rb") as f:
        if f.read(8) != PNG_MAGIC:
            raise SystemExit("entry.png is not a PNG file")


def main() -> int:
    check_source()
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    target = os.path.join(out, "entry.png")
    shutil.copyfile(SOURCE, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
