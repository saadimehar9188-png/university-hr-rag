import re


class DocumentCleaner:
    """Clean extracted document text while preserving page metadata."""

    def clean(self, pages: list[dict]) -> list[dict]:
        """Clean the text of each extracted page."""

        cleaned_pages = []

        for page in pages:
            text = page["text"]

            text = self._normalize_whitespace(text)
            text = self._remove_empty_lines(text)

            if not text:
                continue

            cleaned_pages.append(
                {
                    "text": text,
                    "metadata": page["metadata"],
                }
            )

        return cleaned_pages

    @staticmethod
    def _normalize_whitespace(text: str) -> str:
        """Normalize spaces and tabs without changing line structure."""

        text = text.replace("\t", " ")
        text = re.sub(r"[ ]{2,}", " ", text)

        return text.strip()

    @staticmethod
    def _remove_empty_lines(text: str) -> str:
        """Remove unnecessary blank lines."""

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        return "\n".join(lines)