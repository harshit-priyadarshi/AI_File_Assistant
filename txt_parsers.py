def extract_text(file_path: str) -> str:
    """
    Reads a text file and returns its contents as a string.

    Args:
        file_path: Path to the .txt file.

    Returns:
        The contents of the file as a string.
    """
    if not file_path:
        raise ValueError("File path cannot be empty.")
    if not file_path.lower().endswith(".txt"):
        raise ValueError("Invalid file format. Please provide a .txt file.")
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text