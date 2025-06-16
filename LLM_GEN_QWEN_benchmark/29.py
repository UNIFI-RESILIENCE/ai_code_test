from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    # Return a list comprehension that filters strings by the given prefix
    return [s for s in strings if s.startswith(prefix)]