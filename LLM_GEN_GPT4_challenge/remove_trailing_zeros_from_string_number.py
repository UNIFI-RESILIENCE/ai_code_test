def remove_trailing_zeros(num: str) -> str:
    """
    Removes trailing zeros from a numeric string representation of a positive integer.

    Parameters:
    num (str): A string representing a positive integer.

    Returns:
    str: Modified string with trailing zeros removed.
    """

    # Use rstrip to remove trailing '0' characters from the end of the string
    return num.rstrip('0')
```