DISCLAIMER = (
    "This tool provides informational summaries only and does not constitute "
    "legal advice. Consult a qualified attorney for legal guidance."
)


def append_disclaimer(answer: str) -> str:
    """Append the fixed legal disclaimer to the answer text.

    Args:
        answer: The answer text to append the disclaimer to.

    Returns:
        The answer text followed by a newline and the DISCLAIMER constant.
    """
    return f"{answer}\n{DISCLAIMER}"
