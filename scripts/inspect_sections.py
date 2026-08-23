from pathlib import Path

from app.ingestion.cleaner import DocumentCleaner
from app.ingestion.loader import PDFLoader


def main():
    document_path = Path(
        "data/documents/Employee_Handbook.pdf"
    )

    loader = PDFLoader()
    cleaner = DocumentCleaner()

    pages = loader.load(document_path)
    cleaned_pages = cleaner.clean(pages)

    for page in cleaned_pages:
        pdf_page = page["metadata"]["pdf_page"]
        text = page["text"]

        print("=" * 80)
        print(f"PDF PAGE: {pdf_page}")
        print("=" * 80)

        lines = text.splitlines()

        for line_number, line in enumerate(lines, start=1):
            print(f"{line_number:03}: {line}")


if __name__ == "__main__":
    main()