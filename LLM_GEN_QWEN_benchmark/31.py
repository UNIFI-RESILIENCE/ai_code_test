def is_prime(n):
    # Handle cases where n is less than 2
    if n < 2:
        return False
    
    # Handle even numbers greater than 2 separately
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Exclude all other even numbers
    
    # Check for factors from 3 to the square root of n
    # We check only odd numbers (hence i += 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False  # Found a factor, n is not prime
    
    return True  # No factors found, n is prime