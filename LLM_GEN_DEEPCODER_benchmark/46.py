def fib4(n: int) -> int:
    """
    Computes the n-th element of the Fib4 sequence iteratively.
    
    The Fib4 sequence is defined as:
    - fib4(0) = 0
    - fib4(1) = 0
    - fib4(2) = 2
    - fib4(3) = 0
    - fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4
    
    Args:
        n: The index of the Fib4 sequence to compute.
        
    Returns:
        The n-th element of the Fib4 sequence.
        
    Examples:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
        >>> fib4(7)
        14
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Base cases
    if n == 0 or n == 1 or n == 3:
        return 0
    elif n == 2:
        return 2
    
    # Initialize the first four values
    fib = [0, 0, 2, 0]
    
    # Compute from fib4(4) up to fib4(n)
    for i in range(4, n + 1):
        next_val = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4]
        fib.append(next_val)
    
    return fib[n]