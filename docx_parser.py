import docx


def extract_text(file_path: str) -> str:
    """
    Reads a DOCX file and returns its contents as a string.

    Args:
        file_path: Path to the .docx file.

    Returns:
        The contents of the file as a string.
    """
    if not file_path:
        raise ValueError("File path cannot be empty.")
    if not file_path.lower().endswith(".docx"):
        raise ValueError("Invalid file format. Please provide a .docx file.")
    document = docx.Document(file_path)
    text_list = []
    for paragraph in document.paragraphs:
        text_list.append(paragraph.text)
    return "\n\n".join(text_list)
