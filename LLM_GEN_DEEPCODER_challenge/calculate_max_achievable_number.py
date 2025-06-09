def maximum_achievable(num: int, t: int) -> int:
    """
    Calculate the maximum achievable number based on the given num and t.
    
    The key observation is that each operation allows the achievable number x 
    to differ from num by 2 (since both x and num change by 1 in opposite directions).
    Therefore, the maximum achievable x is num + 2 * t.
    
    Args:
        num: The base integer to which x should be matched.
        t: The number of operations allowed.
    
    Returns:
        The maximum achievable number x.
    """
    return num + 2 * t