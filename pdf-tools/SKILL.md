---
name: pdf-tools
description: PDF manipulation utilities for rotating, merging, and extracting pages. Use when users need to rotate PDF pages, combine multiple PDFs, or extract specific pages from a PDF.
license: MIT
---

# PDF Tools

Efficient PDF manipulation using bundled Python scripts.

## Available Operations

### Rotate Pages

Rotate pages in a PDF by 90, 180, or 270 degrees.

```bash
python /home/ubuntu/skills/pdf-tools/scripts/rotate_pdf.py <input.pdf> <output.pdf> <rotation> [pages]
```

**Parameters:**
- `rotation`: 90, 180, or 270 degrees
- `pages`: (optional) "all" (default), "1,3,5" (specific pages), or "1-5" (range)

**Example:**
```bash
python /home/ubuntu/skills/pdf-tools/scripts/rotate_pdf.py report.pdf report_rotated.pdf 90 1-3
```

### Merge PDFs

Combine multiple PDF files into a single PDF.

```bash
python /home/ubuntu/skills/pdf-tools/scripts/merge_pdfs.py <output.pdf> <input1.pdf> <input2.pdf> [input3.pdf ...]
```

**Example:**
```bash
python /home/ubuntu/skills/pdf-tools/scripts/merge_pdfs.py combined.pdf chapter1.pdf chapter2.pdf chapter3.pdf
```

### Extract Pages

Extract specific pages from a PDF into a new file.

```bash
python /home/ubuntu/skills/pdf-tools/scripts/extract_pages.py <input.pdf> <output.pdf> <pages>
```

**Parameters:**
- `pages`: "1,3,5" (specific pages) or "1-5" (range)

**Example:**
```bash
python /home/ubuntu/skills/pdf-tools/scripts/extract_pages.py document.pdf summary.pdf 1,5-7,10
```

## Usage Guidelines

- Always use absolute paths for file arguments
- Scripts automatically install `pypdf` dependency if missing
- Verify input files exist before running scripts
- Page numbers are 1-indexed (first page is 1, not 0)
