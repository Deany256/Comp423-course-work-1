from typing import List, Set


def spotting_word(user_input: str, keywords: List[str]) -> bool:
    """Checks for Words from a list are within a string

    Args:
        user_input (str): A none-empty string
        keywords (List[str]): A list of strings

    Returns:
        bool: Will return True if an item from the list is within the string
    """
    if set(keywords) & set(user_input.split()):
        return True
    else:
        return False
