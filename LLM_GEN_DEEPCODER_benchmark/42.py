def incr_list(l: list):
    """
    Increment each element in the input list by 1 and return the new list.
    
    Args:
        l: Input list of integers.
    
    Returns:
        A new list where each element is incremented by 1.
    
    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]