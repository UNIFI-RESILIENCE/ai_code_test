from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    # Use list comprehension to filter only elements that are of type int
    return [value for value in values if isinstance(value, int)]