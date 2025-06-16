def unique(l: list):
    """Return sorted unique elements in a list
    
    Args:
        l: A list of elements (can contain duplicates)
    
    Returns:
        A sorted list of unique elements from the input list
    
    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates, then back to a list
    unique_elements = list(set(l))
    
    # Sort the unique elements and return
    return sorted(unique_elements)