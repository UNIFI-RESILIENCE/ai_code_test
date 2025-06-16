from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    # Use a list comprehension to filter strings containing the specified substring
    return [s for s in strings if substring in s]