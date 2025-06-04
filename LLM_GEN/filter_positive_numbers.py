Here's the optimum implementation for the function get_positive based on the problem description:

def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [x for x in l if x > 0]

This implementation uses a list comprehension to efficiently filter and return only the positive numbers (greater than 0) from the input list. It meets the given examples and passes the provided test cases.