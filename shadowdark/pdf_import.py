import pymupdf as fitz  # PyMuPDF
import os
import sys


def pdf_pages_to_images(
    pdf_path,
    output_dir,0
    pages=None,  # list of 0-based page numbers, or None for all pages
    dpi=300,
):
    os.makedirs(output_dir, exist_ok=True)

    doc = fitz.open(pdf_path)

    zoom = dpi / 72  # 72 DPI is PDF default
    matrix = fitz.Matrix(zoom, zoom)

    if pages is None:
        pages = range(len(doc))

    for page_num in pages:
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=matrix, alpha=False)

        output_path = os.path.join(output_dir, f"page_{page_num + 1}.png")
        pix.save(output_path)
        print(f"Saved: {output_path}")

    doc.close()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pdf_to_images.py input.pdf output_dir [page_numbers]")
        print("Example: python pdf_to_images.py file.pdf images 1,2,5")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_dir = sys.argv[2]

    if len(sys.argv) >= 4:
        # User provides pages as 1-based, comma-separated
        pages = [int(p) - 1 for p in sys.argv[3].split(",")]
    else:
        pages = None

    pdf_pages_to_images(pdf_path, output_dir, pages)
