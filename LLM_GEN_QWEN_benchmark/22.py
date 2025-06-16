from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    # Use a list comprehension to filter and collect only integers from the input list
    return [value for value in values if isinstance(value, int)]

# Example usage:
# print(filter_integers(['a', 3.14, 5]))  # Output: [5]
# print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]