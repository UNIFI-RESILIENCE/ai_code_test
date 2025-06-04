Here's the optimum implementation of the is_prime function that satisfies all the test cases efficiently:

def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

This implementation first handles edge cases (n ≤ 1 and even numbers), and then checks divisibility only up to the square root of n using odd numbers, which is efficient for large inputs.