"""Add a centered title to an image and save it as a compressed JPEG.

The title is centered horizontally over the full image width and can be drawn either
on an added bar above the image (``--mode bar``, the default) or as an overlay band
across the top of the image (``--mode overlay``). Long titles are word-wrapped to fit
the image width. The output is always JPEG, and the compression level is set with
``--quality`` (Pillow quality, 1 to 95, lower means a smaller file).

Examples:
  & "C:\\Users\\Ninya\\miniconda3\\envs\\pytorch312\\python.exe" add_title.py \
      images\\jpgs\\figure3.1.1.jpg "Document head learning rate" \
      -o images\\jpgs\\figure3.1.1_titled.jpg --quality 85

  & "C:\\Users\\Ninya\\miniconda3\\envs\\pytorch312\\python.exe" add_title.py \
      images\\jpgs\\figure3.1.1.jpg "Document head learning rate" \
      --mode overlay --quality 80
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


# Fonts tried in order; the first one present on the machine is used. A built-in
# bitmap font is the last resort so the tool still runs without a TrueType font.
FONT_CANDIDATES = (
    "C:/Windows/Fonts/arial.ttf",
    "C:/Windows/Fonts/segoeui.ttf",
    "C:/Windows/Fonts/calibri.ttf",
    "C:/Windows/Fonts/verdana.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/Library/Fonts/Arial.ttf",
)


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Return a scalable font at ``size``, or Pillow's default if none is found."""
    for candidate in FONT_CANDIDATES:
        if Path(candidate).exists():
            try:
                return ImageFont.truetype(candidate, size)
            except OSError:
                continue
    return ImageFont.load_default()


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font, max_width: int) -> list[str]:
    """Greedy word-wrap of ``text`` so each line fits within ``max_width`` pixels.

    A single word wider than ``max_width`` is still emitted on its own line rather
    than split, so an unbreakable token is never dropped.
    """
    lines: list[str] = []
    current = ""
    for word in text.split():
        trial = word if not current else f"{current} {word}"
        width = draw.textbbox((0, 0), trial, font=font)[2]
        if width <= max_width or not current:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def add_title(
    image_path: Path,
    title: str,
    output_path: Path,
    *,
    quality: int = 90,
    font_size: int | None = None,
    color: str = "black",
    background: str = "white",
    mode: str = "bar",
) -> Path:
    """Compose ``title`` onto ``image_path`` and write ``output_path`` as JPEG.

    In ``bar`` mode the canvas grows by a title block at the top. In ``overlay`` mode
    an opaque band of the same height is drawn over the top of the image.
    """
    image = Image.open(image_path).convert("RGB")
    width, _ = image.size

    size = font_size or max(16, int(width * 0.03))
    font = load_font(size)
    measure = ImageDraw.Draw(image)

    ascent, descent = font.getmetrics()
    line_height = ascent + descent
    lines = wrap_text(measure, title, font, int(width * 0.92))

    pad = max(8, int(line_height * 0.3))
    block_height = pad + line_height * len(lines) + pad

    if mode == "bar":
        canvas = Image.new("RGB", (width, image.height + block_height), background)
        canvas.paste(image, (0, block_height))
        draw = ImageDraw.Draw(canvas)
        top = pad
    else:  # overlay
        canvas = image
        draw = measure
        draw.rectangle([0, 0, width, block_height], fill=background)
        top = pad

    y = top
    for line in lines:
        line_width = draw.textbbox((0, 0), line, font=font)[2]
        draw.text(((width - line_width) // 2, y), line, font=font, fill=color)
        y += line_height

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path, format="JPEG", quality=quality, optimize=True)
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("image", type=Path, help="input image path")
    parser.add_argument("title", nargs="+", help="title text (words are joined with spaces)")
    parser.add_argument("-o", "--output", type=Path, default=None,
                        help="output JPEG path (default: <image stem>_titled.jpg)")
    parser.add_argument("-q", "--quality", type=int, default=90,
                        help="Pillow JPEG quality, 1 to 95 (lower is smaller)")
    parser.add_argument("--font-size", type=int, default=None,
                        help="title font size in pixels (default: 3%% of image width)")
    parser.add_argument("--color", default="black", help="title text colour")
    parser.add_argument("--background", default="white",
                        help="title block or band background colour")
    parser.add_argument("--mode", choices=("bar", "overlay"), default="bar",
                        help="draw the title on an added bar or over the image")
    args = parser.parse_args()

    if not args.image.exists():
        raise SystemExit(f"input image not found: {args.image}")
    if not 1 <= args.quality <= 95:
        raise SystemExit("quality must be between 1 and 95")

    output = args.output or args.image.with_name(f"{args.image.stem}_titled.jpg")
    written = add_title(
        args.image,
        " ".join(args.title),
        output,
        quality=args.quality,
        font_size=args.font_size,
        color=args.color,
        background=args.background,
        mode=args.mode,
    )
    print(f"wrote {written}")


if __name__ == "__main__":
    main()
