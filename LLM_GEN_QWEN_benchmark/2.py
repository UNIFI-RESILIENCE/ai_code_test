def truncate_number(number: float) -> float:
    # Calculate the integer part of the number using int() which truncates towards zero
    integer_part = int(number)
    
    # Subtract the integer part from the original number to get the decimal part
    decimal_part = number - integer_part
    
    # Return the decimal part of the number
    return decimal_part