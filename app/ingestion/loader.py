from pathlib import Path

import pymupdf

from app.models.document import DocumentMetadata, DocumentPage


class PDFLoader:
    """Load text content from a PDF document."""

    def load(self, file_path: Path) -> list[DocumentPage]:
        """Extract text from each page of a PDF."""

        if not file_path.exists():
            raise FileNotFoundError(
                f"Document not found: {file_path}"
            )

        if file_path.suffix.lower() != ".pdf":
            raise ValueError(
                f"Unsupported file type: {file_path.suffix}"
            )

        pages = []

        with pymupdf.open(file_path) as document:
            for page_number, page in enumerate(document, start=1):
                text = page.get_text("text").strip()

                pages.append(
                    DocumentPage(
                        text=text,
                        metadata=DocumentMetadata(
                            source=file_path.name,
                            pdf_page=page_number,
                        ),
                    )
                )

        return pages