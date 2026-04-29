#!/usr/bin/env python3
"""
Merge multiple PDF files into a single PDF.
"""
import sys
from pypdf import PdfWriter


def merge_pdfs(output_path: str, *input_paths: str):
    """
    Merge multiple PDFs into one.
    
    Args:
        output_path: Path to output merged PDF
        input_paths: Paths to input PDFs (in order)
    """
    if len(input_paths) < 2:
        raise ValueError("Need at least 2 PDFs to merge")
    
    writer = PdfWriter()
    
    for pdf_path in input_paths:
        writer.append(pdf_path)
    
    with open(output_path, "wb") as f:
        writer.write(f)
    
    print(f"✅ Merged {len(input_paths)} PDFs → {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: merge_pdfs.py <output.pdf> <input1.pdf> <input2.pdf> [input3.pdf ...]")
        sys.exit(1)
    
    output_pdf = sys.argv[1]
    input_pdfs = sys.argv[2:]
    
    merge_pdfs(output_pdf, *input_pdfs)
