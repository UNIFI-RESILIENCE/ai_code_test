import math

def is_prime(num: int) -> bool:
    """Check if a number is prime.
    
    Args:
        num: The number to check for primality.
        
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    # Check divisibility up to sqrt(num)
    max_divisor = math.isqrt(num) + 1
    for i in range(3, max_divisor, 2):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    """Return the n-th number that is both a Fibonacci number and prime.
    
    Args:
        n: The index of the desired prime Fibonacci number (1-based).
        
    Returns:
        int: The n-th prime Fibonacci number.
        
    Raises:
        ValueError: If n is not positive.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    count = 0
    a, b = 1, 1  # Initialize Fibonacci sequence
    
    while True:
        # Generate next Fibonacci number
        a, b = b, a + b
        
        # Check if the Fibonacci number is prime
        if is_prime(a):
            count += 1
            if count == n:
                return a