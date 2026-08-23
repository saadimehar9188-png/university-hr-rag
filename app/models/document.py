from dataclasses import dataclass, field


@dataclass
class DocumentMetadata:
    """Metadata describing the source of a document."""

    source: str
    pdf_page: int


@dataclass
class DocumentPage:
    """A single extracted page from a source document."""

    text: str
    metadata: DocumentMetadata


@dataclass
class DocumentChunk:
    """A searchable chunk created from a document."""

    text: str
    metadata: DocumentMetadata
    section: str | None = None
    chunk_id: str | None = None