from pathlib import Path

from app.ingestion.loader import PDFLoader


def main():
    document_path = Path(
        "data/documents/Employee_Handbook.pdf"
    )

    loader = PDFLoader()
    pages = loader.load(document_path)

    print(f"Pages loaded: {len(pages)}")

    for page in pages[:3]:
        print("-" * 60)
        print(f"PDF page: {page.metadata.pdf_page}")
        print(page.text[:500])


if __name__ == "__main__":
    main()