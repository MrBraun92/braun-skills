#!/usr/bin/env python3
"""
Extract specific pages from a PDF into a new PDF.
"""
import sys
from pypdf import PdfReader, PdfWriter


def extract_pages(input_path: str, output_path: str, pages: str):
    """
    Extract pages from a PDF.
    
    Args:
        input_path: Path to input PDF
        output_path: Path to output PDF
        pages: Page selection - "1,3,5" or "1-5"
    """
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    # Parse page selection
    if "-" in pages:
        start, end = map(int, pages.split("-"))
        page_indices = range(start - 1, end)
    else:
        page_indices = [int(p) - 1 for p in pages.split(",")]
    
    # Extract selected pages
    for i in page_indices:
        if 0 <= i < len(reader.pages):
            writer.add_page(reader.pages[i])
    
    with open(output_path, "wb") as f:
        writer.write(f)
    
    print(f"✅ Extracted {len(list(page_indices))} pages → {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: extract_pages.py <input.pdf> <output.pdf> <pages>")
        print("  pages: '1,3,5' or '1-5'")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    pages = sys.argv[3]
    
    extract_pages(input_pdf, output_pdf, pages)
