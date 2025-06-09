def truncate_number(number: float) -> float:
    # Get the integer part by converting the number to an integer (truncates toward zero)
    integer_part = int(number)

    # Subtract the integer part from the original number to get the decimal part
    decimal_part = number - integer_part

    return decimal_part