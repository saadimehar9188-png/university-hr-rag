from pathlib import Path

from app.ingestion.cleaner import DocumentCleaner
from app.ingestion.loader import PDFLoader


def main():
    document_path = Path(
        "data/documents/Employee_Handbook.pdf"
    )

    loader = PDFLoader()
    pages = loader.load(document_path)

    cleaner = DocumentCleaner()
    cleaned_pages = cleaner.clean(pages)

    print(f"Pages before cleaning: {len(pages)}")
    print(f"Pages after cleaning: {len(cleaned_pages)}")

    for page in cleaned_pages[:3]:
        print("-" * 60)
        print(f"PDF page: {page['metadata']['pdf_page']}")
        print(page["text"][:500])


if __name__ == "__main__":
    main()