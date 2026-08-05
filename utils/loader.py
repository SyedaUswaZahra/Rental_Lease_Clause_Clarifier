from langchain_community.document_loaders import PyPDFLoader


def load_lease_text(source: str, is_pdf: bool = True) -> str:
    """Load lease text from a PDF file path or pasted plain text.

    Args:
        source: If is_pdf is True, a file path to the PDF; otherwise pasted lease text.
        is_pdf: Whether the source is a PDF file path.

    Returns:
        Raw lease text as a single string.
    """
    if is_pdf:
        loader = PyPDFLoader(source)
        documents = loader.load()
        raw_text = "\n".join(page.page_content for page in documents)
        return raw_text
    return source
