def prime_fib(n: int):
    """
    Returns the n-th number that is both a Fibonacci number and a prime number.
    """
    def is_prime(num: int) -> bool:
        """Check whether a given number is prime."""
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    fib_primes = []  # List to store Fibonacci numbers that are prime
    a, b = 0, 1       # Initialize first two Fibonacci numbers

    while len(fib_primes) < n:
        a, b = b, a + b  # Generate next Fibonacci number
        if is_prime(a):
            fib_primes.append(a)  # Add to list if number is prime

    return fib_primes[-1]  # Return the n-th Fibonacci prime number