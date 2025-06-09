def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_fibonacci(limit: int) -> list:
    """Generate a list of Fibonacci numbers up to a certain limit."""
    fibs = [0, 1]
    while True:
        next_fib = fibs[-1] + fibs[-2]
        if next_fib > limit:
            break
        fibs.append(next_fib)
    return fibs


def prime_fib(n: int) -> int:
    """Return the n-th Fibonacci number that is also prime."""
    # Start with a reasonable limit for Fibonacci numbers
    limit = 10**18  # This limit can be adjusted based on requirements
    fibs = generate_fibonacci(limit)
    
    # Filter Fibonacci numbers to get only the prime ones
    prime_fibs = [f for f in fibs if is_prime(f)]
    
    # Return the n-th prime Fibonacci number
    return prime_fibs[n - 1]


# Test cases
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
assert prime_fib(6) == 233
assert prime_fib(7) == 1597
assert prime_fib(8) == 28657
assert prime_fib(9) == 514229
assert prime_fib(10) == 433494437