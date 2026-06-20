#!/usr/bin/env python3
"""Build all PDFs (per group + combined) and 150dpi previews."""
import os, sys
import weasyprint
import pypdfium2 as pdfium

sys.path.insert(0, os.path.dirname(__file__))
from lots import LOTS, GROUPS
from render import build_html

OUT = os.path.abspath("./outputs")
PREV = os.path.abspath("./previews")
os.makedirs(OUT, exist_ok=True)
os.makedirs(PREV, exist_ok=True)


def write_pdf(lots, path):
    html = build_html(lots)
    weasyprint.HTML(string=html, base_url=".").write_pdf(path)
    print("PDF", path, len(lots), "pages")


def main():
    # Per-group PDFs
    for stem, (a, b) in GROUPS:
        write_pdf(LOTS[a:b], os.path.join(OUT, f"{stem}.pdf"))
    # Combined
    combined = os.path.join(OUT, "Датский_все_планировки.pdf")
    write_pdf(LOTS, combined)

    # Previews at 150 dpi from combined PDF
    pdf = pdfium.PdfDocument(combined)
    scale = 150 / 72
    for i in range(len(pdf)):
        page = pdf[i]
        bmp = page.render(scale=scale)
        img = bmp.to_pil()
        img.save(os.path.join(PREV, f"prev_{i+1:02d}.png"))
    print("PREVIEWS", len(pdf))
    pdf.close()


if __name__ == "__main__":
    main()
