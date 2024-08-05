from datetime import datetime
from typing import Optional


def format_to_date(date: Optional[str]) -> str:
    if date is None:
        return None
    try:
        return datetime.fromisoformat(date).strftime("%d/%m/%Y")
    except ValueError:
        print("Invalid date format")
        return "Invalid Date"
    except TypeError:
        print("Date is None")
        return None


def convert_date_to_json(date_str: str) -> str:
    """
    Converts a date string in the format MM/DD/YY to a JSON serializable ISO 8601 string.

    Args:
        date_str (str): The date string in MM/DD/YY format.

    Returns:
        str: The ISO 8601 formatted date string, serialized to JSON.
    """
    try:
        date_obj = datetime.strptime(date_str, "%m/%d/%y")

        iso_date_str = date_obj.isoformat()

        return iso_date_str
    except ValueError:
        print("Invalid date format")
        return None


# print(convert_date_to_json("08/23/23"))
