from pathlib import Path

from app.ingestion.loader import PDFLoader


def main():
    document_path = Path(
        "data/documents/Employee_Handbook.pdf"
    )

    loader = PDFLoader()
    spans = loader.inspect_layout(document_path)

    for span in spans:
        if span["pdf_page"] in {9, 10, 11, 12, 13, 14}:
            print(
                f"PAGE {span['pdf_page']:02} | "
                f"SIZE {span['size']:5.1f} | "
                f"FLAGS {span['flags']:3} | "
                f"FONT {span['font']:<25} | "
                f"{span['text']}"
            )


if __name__ == "__main__":
    main()