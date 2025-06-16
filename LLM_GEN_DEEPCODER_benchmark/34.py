def unique(l: list):
    """Return sorted unique elements in a list
    
    Args:
        l: Input list containing elements (may include duplicates)
    
    Returns:
        A new list with unique elements sorted in ascending order
    
    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates, then back to a list
    unique_elements = list(set(l))
    
    # Sort the unique elements in ascending order
    unique_elements.sort()
    
    return unique_elements