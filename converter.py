import argparse
from pathlib import Path

try:
    from pdf2docx import Converter as PDF2DocxConverter
except ImportError as e:
    PDF2DocxConverter = None

try:
    from docx2pdf import convert as docx2pdf_convert
except ImportError:
    docx2pdf_convert = None

def pdf_to_docx(pdf_path: Path, docx_path: Path) -> None:
    """Convert a PDF file to DOCX."""
    if PDF2DocxConverter is None:
        raise RuntimeError("pdf2docx package is not installed")
    pdf_file = str(pdf_path)
    docx_file = str(docx_path)
    converter = PDF2DocxConverter(pdf_file)
    try:
        converter.convert(docx_file)
    finally:
        converter.close()

def docx_to_pdf(docx_path: Path, pdf_path: Path) -> None:
    """Convert a DOCX file to PDF."""
    if docx2pdf_convert is None:
        raise RuntimeError("docx2pdf package is not installed")
    docx2pdf_convert(str(docx_path), str(pdf_path))

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert between PDF and DOCX.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    pdf2docx_parser = subparsers.add_parser("pdf2docx", help="Convert PDF to DOCX")
    pdf2docx_parser.add_argument("input", type=Path, help="Input PDF file")
    pdf2docx_parser.add_argument("output", type=Path, help="Output DOCX file")

    docx2pdf_parser = subparsers.add_parser("docx2pdf", help="Convert DOCX to PDF")
    docx2pdf_parser.add_argument("input", type=Path, help="Input DOCX file")
    docx2pdf_parser.add_argument("output", type=Path, help="Output PDF file")

    return parser.parse_args()

def main() -> None:
    args = parse_args()
    if args.command == "pdf2docx":
        pdf_to_docx(args.input, args.output)
    elif args.command == "docx2pdf":
        docx_to_pdf(args.input, args.output)

if __name__ == "__main__":
    main()
