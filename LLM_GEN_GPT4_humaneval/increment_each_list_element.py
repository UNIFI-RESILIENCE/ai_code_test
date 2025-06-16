def incr_list(l: list):
    # Use list comprehension to increment each element by 1
    return [x + 1 for x in l]


METADATA = {}


def check(candidate):
    # Test case: empty list should return an empty list
    assert candidate([]) == []
    # Test case: simple list with descending integers
    assert candidate([3, 2, 1]) == [4, 3, 2]
    # Test case: complex list with various integers
    assert candidate([5, 2, 5, 2, 3, 3, 9, 0, 123]) == [6, 3, 6, 3, 4, 4, 10, 1, 124]