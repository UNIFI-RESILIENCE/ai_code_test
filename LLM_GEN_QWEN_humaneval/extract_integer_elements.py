from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    # Use a list comprehension to filter out only integer types from the input list
    return [value for value in values if isinstance(value, int)]


# Metadata for reference or additional information
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    # Test case 1: Empty list should return an empty list
    assert candidate([]) == []
    
    # Test case 2: Mixed types, should return only integers
    assert candidate([4, {}, [], 23.2, 9, 'adasd']) == [4, 9]
    
    # Test case 3: Multiple integers with non-integer strings, should return only integers
    assert candidate([3, 'c', 3, 3, 'a', 'b']) == [3, 3, 3]


# Run the check function to validate the filter_integers function
check(filter_integers)