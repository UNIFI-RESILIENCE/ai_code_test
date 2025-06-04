To solve the problem, we need to find the n-th number that is both:

1. A Fibonacci number.
2. A prime number.

This means we generate Fibonacci numbers one by one and test each to see if it's prime. Once we've found n such numbers, we return the last one.

Here is the optimal implementation:

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    def is_prime(x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        for i in range(3, int(x**0.5) + 1, 2):
            if x % i == 0:
                return False
        return True

    a, b = 1, 1
    count = 0
    while True:
        a, b = b, a + b
        if is_prime(a):
            count += 1
            if count == n:
                return a

This function uses a helper is_prime to check primality efficiently and iterates through the Fibonacci sequence until n prime Fibonacci numbers are found.