"""
apt install ocrmypdf
"""

import os
import subprocess
from util import download
from PyPDF2 import PdfFileReader, PdfFileWriter


def is_typeset(pdf_path):
    """Hack to check if a PDF is typeset or scanned.
    If no fonts are found assume it's scanned."""
    res = subprocess.run(['pdffonts', pdf_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return bool([l for l in res.stdout.decode('utf8').split('\n')[2:] if l])


def ocr_pdf(pdf_path):
    """Apply OCR to a scanned PDF to add
    a searchable layer using `ocrmypdf`.
    Returns extracted plain text."""
    subprocess.run(['ocrmypdf', '--sidecar', '/tmp/pdf_txt.txt', pdf_path, '/tmp/pdf_ocr.pdf'])
    os.rename('/tmp/pdf_ocr.pdf', pdf_path)
    with open('/tmp/pdf_txt.txt') as f:
        text = f.read()
    return text


def extract_metadata(pdf_path):
    """Attempt to extract metadata from a PDF.
    Not super reliable, but works sometimes."""
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
    return pdf.getDocumentInfo()


def update_metadata(pdf_path, metadata):
    """Update the metadata of a PDF"""
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
    writer = PdfFileWriter()
    writer.appendPagesFromReader(pdf)
    meta = pdf.getDocumentInfo()
    meta.update(metadata)
    writer.addMetadata(meta)
    with open(pdf_path, 'wb') as f:
        writer.write(f)


if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    pdf_url = args

    library_path = '/home/ftseng/docs/library/pdfs'
    pdf_path = download(pdf_url, library_path)
    if not is_typeset(pdf_path):
        ocr_pdf(pdf_path)
    extract_metadata(pdf_path)