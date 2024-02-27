# PDF Merger

A simple Python script to merge two PDF files into one.

## Description

This script allows you to merge a cover PDF and a footer PDF, or any two PDFs, into a single PDF file. The cover PDF will be placed at the beginning of the merged file, followed by the footer PDF.

## Usage

To use this script, run it from the command line and provide the file paths of the cover PDF and the footer PDF as arguments. Optionally, you can specify the output file path using the `-o` or `--output` flag.

```bash
python merge_pdf.py cover.pdf footer.pdf -o output.pdf
