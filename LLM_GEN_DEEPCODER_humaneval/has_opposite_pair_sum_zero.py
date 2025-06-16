def pairs_sum_to_zero(l):
    """
    Checks if there are two distinct elements in the list that sum to zero.
    
    Args:
        l: List of integers to check
        
    Returns:
        True if such a pair exists, False otherwise
        
    Approach:
        - Uses a set for O(1) lookups
        - For each element, checks if its negative exists in the set
        - Handles edge cases like single-element lists and multiple zeros
    """
    # Handle edge case of empty list or single element
    if len(l) < 2:
        return False
    
    seen = set()
    
    for num in l:
        # Check if the negative of current number exists in seen
        if -num in seen:
            # Ensure they're distinct elements (handles zero case)
            if num != 0 or l.count(0) > 1:
                return True
        seen.add(num)
    
    return False