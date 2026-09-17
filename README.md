# PDF Merger Script

## Overview

This Python script merges all PDF files located in a specified folder into a single PDF file named `merged_output.pdf`.

The script uses the `pypdf` library to read and combine PDF documents automatically.

---

## Features

- Automatically scans a folder for PDF files.
- Merges all PDF files into a single document.
- Preserves the original page order within each PDF.
- Generates a merged output file in the same folder.
- Simple and lightweight implementation.

---

## Requirements

- Python 3.13 (or compatible version)
- pypdf library

Install the required package:

```bash
pip install pypdf
```

---

## Folder Structure

```text
Project Individual/
│
├── pdf/
│   ├── File1.pdf
│   ├── File2.pdf
│   ├── File3.pdf
│   └── merged_output.pdf  (Generated)
│
└── merge_pdf.py
```

---

