import re


class SectionDetector:
    """Detect likely section headings in cleaned document pages."""

    def detect(self, text: str) -> list[dict]:
        """Return lines that appear to be section headings."""

        headings = []

        for line_number, line in enumerate(
            text.splitlines(),
            start=1,
        ):
            normalized_line = line.strip()

            if not normalized_line:
                continue

            if self._looks_like_heading(normalized_line):
                headings.append(
                    {
                        "line_number": line_number,
                        "title": normalized_line,
                    }
                )

        return headings

    @staticmethod
    def _looks_like_heading(line: str) -> bool:
        """Determine whether a line looks like a heading."""

        if len(line) > 80:
            return False

        if line.isupper():
            return True

        return False