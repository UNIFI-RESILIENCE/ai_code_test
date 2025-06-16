def median(l: list):
    """
    Calculate the median of a list of numbers.
    
    Args:
        l: List of numbers (integers or floats).
        
    Returns:
        The median value as a float if the list has an even number of elements,
        or as an int if the list has an odd number of elements.
        
    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    if not l:
        raise ValueError("List must not be empty")
    
    sorted_l = sorted(l)
    n = len(sorted_l)
    mid = n // 2
    
    if n % 2 == 1:
        return sorted_l[mid]
    else:
        return (sorted_l[mid - 1] + sorted_l[mid]) / 2