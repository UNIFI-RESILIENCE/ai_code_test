METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def strlen(string: str) -> int:
    # Initialize a counter to zero
    count = 0
    
    # Iterate over each character in the string
    for _ in string:
        # Increment the counter for each character
        count += 1
    
    # Return the total count of characters
    return count

def check(candidate):
    # Test case for an empty string
    assert candidate('') == 0, "Test case for empty string failed"
    
    # Test case for a single character string
    assert candidate('x') == 1, "Test case for single character string failed"
    
    # Test case for a multi-character string
    assert candidate('asdasnakj') == 9, "Test case for multi-character string failed"