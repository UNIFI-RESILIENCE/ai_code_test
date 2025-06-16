from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    # Return a list containing only the elements of type int
    return [value for value in values if isinstance(value, int)]


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    # Test with empty list; should return empty list
    assert candidate([]) == []
    
    # Test with mix of data types; should only include integers
    assert candidate([4, {}, [], 23.2, 9, 'adasd']) == [4, 9]
    
    # Test with repeated integers and non-integer types
    assert candidate([3, 'c', 3, 3, 'a', 'b']) == [3, 3, 3]