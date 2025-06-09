from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:  # Check if the input list is empty
        return None  # Return None for an empty list

    # Initialize the longest_string with the first string in the list
    longest_string = strings[0]

    # Iterate over the strings starting from the second one
    for string in strings[1:]:
        # Update longest_string if a longer string is found
        if len(string) > len(longest_string):
            longest_string = string

    return longest_string  # Return the longest string found