Here is the optimal implementation for the truncate_number function:

def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

This solution uses simple arithmetic: subtracting the integer part of the number from the original number to isolate the decimal part. The use of int() ensures we get the floor of the positive float, which is correct as the number is guaranteed to be positive.