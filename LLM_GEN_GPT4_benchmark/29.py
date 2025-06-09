from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    # Use list comprehension to filter strings that start with the given prefix
    return [s for s in strings if s.startswith(prefix)]