Here's the optimum implementation of the count_distinct_characters function based on the problem description and test cases:

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return len(set(string.lower()))

This function uses set to identify unique characters and lower to make the comparison case-insensitive.