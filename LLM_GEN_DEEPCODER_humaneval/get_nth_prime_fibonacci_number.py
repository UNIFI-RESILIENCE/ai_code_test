def prime_fib(n: int) -> int:
    """Return the nth prime Fibonacci number."""
    if n == 1:
        return 2
    count = 0
    a, b = 1, 1
    while count < n:
        # Generate next Fibonacci number
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b
    return -1  # Shouldn't reach here for valid n

def is_prime(num: int) -> bool:
    """Check if a number is prime using Miller-Rabin test."""
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0:
        return False
    # Write num as d*2^s + 1
    d = num - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    # Test for these bases; sufficient for numbers < 2^64
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in bases:
        if a >= num:
            continue
        x = pow(a, d, num)
        if x == 1 or x == num - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                break
        else:
            return False
    return True