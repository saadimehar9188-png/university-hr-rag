from pathlib import Path

import fitz


class PDFLoader:
    """Load text content from a PDF document."""

    def load(self, file_path: Path) -> list[dict]:
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

        with fitz.open(file_path) as document:
            for page_number, page in enumerate(document, start=1):
                text = page.get_text("text").strip()

                pages.append(
                    {
                        "text": text,
                        "metadata": {
                            "source": file_path.name,
                            "page": page_number,
                        },
                    }
                )

        return pages