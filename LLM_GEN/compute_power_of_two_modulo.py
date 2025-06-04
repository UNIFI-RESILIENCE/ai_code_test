To compute 2ⁿ mod p efficiently, especially for large values of n, we should use Python's built-in pow function with three arguments, which performs modular exponentiation efficiently and avoids overflow issues.

Here's the optimal implementation of the modp function:

def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics)."""
    return pow(2, n, p)

This implementation satisfies the prompt's requirements and handles large exponentiation efficiently using modular exponentiation.