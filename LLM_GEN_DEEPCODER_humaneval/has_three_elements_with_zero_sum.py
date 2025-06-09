def triples_sum_to_zero(l: list):
    """
    Check if there exist three distinct elements in the list that sum to zero.
    
    Args:
        l: List of integers to check.
    
    Returns:
        True if such a triplet exists, False otherwise.
    """
    n = len(l)
    # If the list has fewer than 3 elements, immediately return False
    if n < 3:
        return False
    
    # Sort the list to enable efficient two-pointer approach
    l_sorted = sorted(l)
    
    # Iterate through each element as the potential first element of the triplet
    for i in range(n - 2):
        # Skip duplicate elements to avoid checking the same triplet multiple times
        if i > 0 and l_sorted[i] == l_sorted[i - 1]:
            continue
        
        left = i + 1
        right = n - 1
        target = -l_sorted[i]
        
        # Use two-pointer technique to find pairs that sum to the target
        while left < right:
            current_sum = l_sorted[left] + l_sorted[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
    return False