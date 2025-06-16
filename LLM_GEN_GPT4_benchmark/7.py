from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    # Use list comprehension to filter strings that contain the given substring
    return [s for s in strings if substring in s]