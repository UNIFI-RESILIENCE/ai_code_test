def is_prime(n):
    # Numbers less than 2 are not prime by definition
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # Eliminate even numbers greater than 2
    if n % 2 == 0:
        return False

    # Check for factors from 3 to sqrt(n), skipping even numbers
    sqrt_n = int(n ** 0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False

    # If no divisors were found, the number is prime
    return True