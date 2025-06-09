from typing import List


def all_prefixes(string: str) -> List[str]:
    # Initialize an empty list to store all prefixes
    prefixes = []
    
    # Iterate over the indices of the string
    for i in range(1, len(string) + 1):
        # Append the substring from the start up to the current index to the list
        prefixes.append(string[:i])
    
    # Return the list of prefixes
    return prefixes


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    # Test cases to validate the candidate function
    assert candidate('') == [], "Test with empty string failed"
    assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh'], "Test with 'asdfgh' failed"
    assert candidate('WWW') == ['W', 'WW', 'WWW'], "Test with 'WWW' failed"