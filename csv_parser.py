import csv

def extract_text(file_path: str) -> str:
    """
    Reads a CSV file and returns its contents as a string.

    Args:
        file_path: Path to the .csv file.

    Returns:
        The contents of the file as a string.
    """
    if not file_path:
        raise ValueError("File path cannot be empty.")
    if not file_path.lower().endswith(".csv"):
        raise ValueError("Invalid file format. Please provide a .csv file.")
    

    with open(file_path, "r", encoding="utf-8") as file:
        data = csv.DictReader(file)
        csv_list = []
        for row in data:
            record = []
            for key, value in row.items():
                record.append(f"{key}: {value}")
            csv_list.append("\n".join(record))
    return "\n\n".join(csv_list)



