#!/usr/bin/env python3
"""Convert a PDF file to PNG images (one per page)."""

import argparse
import os
from pdf2image import convert_from_path


def main():
    parser = argparse.ArgumentParser(description="Convert PDF pages to PNG images")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument(
        "-o", "--output-dir", default="output_pages",
        help="Directory to save PNG images (default: output_pages)"
    )
    parser.add_argument(
        "--dpi", type=int, default=300,
        help="DPI for rendering (default: 300)"
    )
    parser.add_argument(
        "--first-page", type=int, default=None,
        help="First page to convert (1-indexed)"
    )
    parser.add_argument(
        "--last-page", type=int, default=None,
        help="Last page to convert (1-indexed)"
    )
    args = parser.parse_args()

    if not os.path.isfile(args.pdf_path):
        print(f"Error: file not found: {args.pdf_path}")
        return

    os.makedirs(args.output_dir, exist_ok=True)

    kwargs = {"dpi": args.dpi}
    if args.first_page:
        kwargs["first_page"] = args.first_page
    if args.last_page:
        kwargs["last_page"] = args.last_page

    print(f"Converting {args.pdf_path} at {args.dpi} DPI...")
    images = convert_from_path(args.pdf_path, **kwargs)

    start = args.first_page or 1
    for i, img in enumerate(images):
        page_num = start + i
        out_path = os.path.join(args.output_dir, f"page_{page_num:04d}.png")
        img.save(out_path, "PNG")
        print(f"  Saved {out_path}")

    print(f"Done — {len(images)} pages saved to {args.output_dir}/")


if __name__ == "__main__":
    main()
