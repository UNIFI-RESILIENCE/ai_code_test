def max_element(l: list):
    """
    Return the maximum element in the given list.
    
    Args:
        l: A list of comparable elements (e.g., integers, floats).
    
    Returns:
        The maximum element in the list.
    
    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not l:
        raise ValueError("List cannot be empty")
    
    max_val = l[0]
    for element in l[1:]:
        if element > max_val:
            max_val = element
    return max_val