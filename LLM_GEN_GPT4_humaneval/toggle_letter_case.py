def flip_case(string: str) -> str:
    # Use the built-in str.swapcase() method to flip the case of all characters in the string
    return string.swapcase()


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    # Test empty string
    assert candidate('') == ''
    # Test a typical string with letters and punctuation
    assert candidate('Hello!') == 'hELLO!'
    # Test a sentence with multiple words and mixed casing
    assert candidate('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'