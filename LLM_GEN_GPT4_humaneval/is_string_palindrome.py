def is_palindrome(text: str) -> bool:
    # A string is a palindrome if it reads the same forwards and backwards.
    # We compare the string with its reverse using slicing.
    return text == text[::-1]


METADATA = {}


def check(candidate):
    assert candidate('') == True  # An empty string is a palindrome
    assert candidate('aba') == True  # Symmetrical around the center
    assert candidate('aaaaa') == True  # All characters are the same
    assert candidate('zbcd') == False  # Not a palindrome
    assert candidate('xywyx') == True  # Palindrome with different characters
    assert candidate('xywyz') == False  # One character off
    assert candidate('xywzx') == False  # Another non-palindrome example