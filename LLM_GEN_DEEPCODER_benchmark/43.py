def pairs_sum_to_zero(l):
    """
    Check if there are two distinct elements in the list that sum to zero.
    
    Args:
        l: List of integers.
    
    Returns:
        bool: True if such a pair exists, False otherwise.
    """
    # Early exit if the list has fewer than 2 elements
    if len(l) < 2:
        return False
    
    seen = set()
    
    for num in l:
        # Check if the negative of the current number exists in the set
        if -num in seen:
            return True
        seen.add(num)
    
    return False