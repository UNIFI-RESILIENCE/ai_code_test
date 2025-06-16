def strlen(string: str) -> int:
    # Return the number of characters in the input string using built-in len function
    return len(string)


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    # Test with empty string
    assert candidate('') == 0
    # Test with single character
    assert candidate('x') == 1
    # Test with longer string
    assert candidate('asdasnakj') == 9