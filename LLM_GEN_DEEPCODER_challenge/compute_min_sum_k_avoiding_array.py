def minimum_sum(n: int, k: int) -> int:
    """
    Constructs a k-avoiding array of length n with the minimum possible sum.
    
    A k-avoiding array ensures no two distinct elements sum to k. The approach is to 
    greedily select the smallest possible integers while avoiding pairs that sum to k.
    
    Args:
        n: The length of the array to construct.
        k: The target sum to avoid for any two distinct elements.
    
    Returns:
        The minimum sum of the constructed k-avoiding array.
    """
    result = []
    current = 1  # Start with the smallest positive integer
    
    while len(result) < n:
        # Check if current can be added without forming a pair that sums to k
        valid = True
        for num in result:
            if num + current == k:
                valid = False
                break
        
        if valid:
            result.append(current)
        
        # Move to the next integer
        current += 1
    
    return sum(result)