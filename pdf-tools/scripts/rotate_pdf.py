#!/usr/bin/env python3
"""
Rotate pages in a PDF file by 90, 180, or 270 degrees.
"""
import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def rotate_pdf(input_path: str, output_path: str, rotation: int, pages: str = "all"):
    """
    Rotate PDF pages.
    
    Args:
        input_path: Path to input PDF
        output_path: Path to output PDF
        rotation: Degrees to rotate (90, 180, 270)
        pages: Page selection - "all", "1,3,5", or "1-5"
    """
    if rotation not in [90, 180, 270]:
        raise ValueError("Rotation must be 90, 180, or 270 degrees")
    
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    # Parse page selection
    if pages == "all":
        page_indices = range(len(reader.pages))
    elif "-" in pages:
        start, end = map(int, pages.split("-"))
        page_indices = range(start - 1, end)
    else:
        page_indices = [int(p) - 1 for p in pages.split(",")]
    
    # Rotate selected pages
    for i, page in enumerate(reader.pages):
        if i in page_indices:
            page.rotate(rotation)
        writer.add_page(page)
    
    with open(output_path, "wb") as f:
        writer.write(f)
    
    print(f"✅ Rotated {len(list(page_indices))} pages by {rotation}° → {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: rotate_pdf.py <input.pdf> <output.pdf> <rotation> [pages]")
        print("  rotation: 90, 180, or 270")
        print("  pages: 'all' (default), '1,3,5', or '1-5'")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    rotation = int(sys.argv[3])
    pages = sys.argv[4] if len(sys.argv) > 4 else "all"
    
    rotate_pdf(input_pdf, output_pdf, rotation, pages)
