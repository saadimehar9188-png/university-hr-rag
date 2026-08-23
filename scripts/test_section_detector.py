from pathlib import Path

from app.ingestion.cleaner import DocumentCleaner
from app.ingestion.loader import PDFLoader
from app.ingestion.section_detector import SectionDetector


def main():
    document_path = Path(
        "data/documents/Employee_Handbook.pdf"
    )

    loader = PDFLoader()
    cleaner = DocumentCleaner()
    detector = SectionDetector()

    pages = loader.load(document_path)
    cleaned_pages = cleaner.clean(pages)

    for page in cleaned_pages:
        pdf_page = page["metadata"]["pdf_page"]
        headings = detector.detect(page["text"])

        if not headings:
            continue

        print("=" * 60)
        print(f"PDF PAGE: {pdf_page}")
        print("=" * 60)

        for heading in headings:
            print(
                f"{heading['line_number']:03}: "
                f"{heading['title']}"
            )


if __name__ == "__main__":
    main()