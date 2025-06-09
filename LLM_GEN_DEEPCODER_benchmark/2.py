def truncate_number(number: float) -> float:
    """
    Extract and return the decimal part of a positive floating-point number.

    The function decomposes the number into its integer part (largest integer smaller than the number)
    and the decimal part (remaining part smaller than 1). The decimal part is returned.

    Args:
        number (float): A positive floating-point number.

    Returns:
        float: The decimal part of the input number.

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    # The decimal part is obtained by subtracting the integer part from the number.
    return number - int(number)