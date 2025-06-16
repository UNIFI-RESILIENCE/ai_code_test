def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n: The number to check.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Notes:
        A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
        This function uses trial division up to the square root of n for efficiency.
    """
    if n <= 1:
        return False
    if n == 2:  # 2 is the smallest and only even prime number
        return True
    if n % 2 == 0:  # Even numbers > 2 are not prime
        return False
    
    # Check for divisors up to the square root of n
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):  # Skip even numbers
        if n % d == 0:
            return False
    return True