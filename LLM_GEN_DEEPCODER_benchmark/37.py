def sort_even(l: list):
    """
    Returns a new list where even indices are sorted in ascending order while odd indices remain unchanged.
    
    Args:
        l: Input list to be processed.
    
    Returns:
        A new list with even indices sorted and odd indices unchanged.
        
    Example:
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    if not l:
        return []
    
    # Extract values at even indices
    even_indices_values = [l[i] for i in range(0, len(l), 2)]
    
    # Sort the even indices values
    sorted_even_values = sorted(even_indices_values)
    
    # Rebuild the list with sorted even values and original odd values
    result = []
    even_idx = 0  # Tracks position in sorted_even_values
    
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(sorted_even_values[even_idx])
            even_idx += 1
        else:
            result.append(l[i])
    
    return result