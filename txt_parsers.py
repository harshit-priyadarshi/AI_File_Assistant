def extract_text(file_path: str) -> str:
    """
    Reads a text file and returns its contents as a string.

    Args:
        file_path: Path to the .txt file.

    Returns:
        The contents of the file as a string.
    """
    
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text