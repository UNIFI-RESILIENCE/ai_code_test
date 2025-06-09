def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, return the decimal part (i.e., the fractional part).

    The decimal part is calculated by subtracting the integer part from the original number.
    
    Args:
        number: A positive floating point number.
        
    Returns:
        float: The decimal part of the number (always less than 1). 
    """
    return number % 1.0


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3.5) == 0.5
    assert abs(candidate(1.33) - 0.33) < 1e-6
    assert abs(candidate(123.456) - 0.456) < 1e-6