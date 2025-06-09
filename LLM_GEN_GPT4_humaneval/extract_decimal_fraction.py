def truncate_number(number: float) -> float:
    # Extract the integer part using int() which truncates towards zero
    integer_part = int(number)
    # Subtract the integer part from the original number to get the decimal part
    decimal_part = number - integer_part
    return decimal_part


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    # Basic test case
    assert candidate(3.5) == 0.5
    # Check with assertion tolerance for floating-point arithmetic
    assert abs(candidate(1.33) - 0.33) < 1e-6
    assert abs(candidate(123.456) - 0.456) < 1e-6