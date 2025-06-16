from typing import List

def all_prefixes(string: str) -> List[str]:
    # Initialize an empty list to hold the prefixes
    prefixes = []
    
    # Loop through characters in the string by index
    for i in range(1, len(string) + 1):
        # Append the substring from the beginning up to the current index
        prefixes.append(string[:i])
    
    return prefixes


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    # Test with empty string; should return an empty list
    assert candidate('') == []
    
    # Test with a standard input
    assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
    
    # Test with repeating characters
    assert candidate('WWW') == ['W', 'WW', 'WWW']