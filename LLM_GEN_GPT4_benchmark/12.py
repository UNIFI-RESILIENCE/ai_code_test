from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    # Check if the list is empty
    if not strings:
        return None

    # Initialize the longest string as the first element
    max_string = strings[0]

    # Iterate through the rest of the list
    for string in strings[1:]:
        # Compare lengths and update the longest string if necessary
        if len(string) > len(max_string):
            max_string = string

    return max_string