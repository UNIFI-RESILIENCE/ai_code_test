def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
        l: List of elements (must be non-empty and elements must be comparable).
    
    Returns:
        The maximum element in the list.
    
    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not l:
        raise ValueError("List must not be empty")
    
    max_val = l[0]
    for num in l[1:]:
        if num > max_val:
            max_val = num
    return max_val