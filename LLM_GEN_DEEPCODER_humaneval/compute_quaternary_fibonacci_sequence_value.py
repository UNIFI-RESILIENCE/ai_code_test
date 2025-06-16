def fib4(n: int) -> int:
    """
    Computes the n-th element of the Fib4 sequence iteratively.
    
    The Fib4 sequence is defined as:
    fib4(0) = 0
    fib4(1) = 0
    fib4(2) = 2
    fib4(3) = 0
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4
    
    Args:
        n: The index of the Fib4 sequence to compute.
        
    Returns:
        The n-th element of the Fib4 sequence.
        
    Examples:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
    """
    if n == 0 or n == 1 or n == 3:
        return 0
    if n == 2:
        return 2
    
    # Initialize the base cases
    fib = [0] * (n + 1)
    fib[0], fib[1], fib[2], fib[3] = 0, 0, 2, 0
    
    # Compute from fib4(4) to fib4(n)
    for i in range(4, n + 1):
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4]
    
    return fib[n]