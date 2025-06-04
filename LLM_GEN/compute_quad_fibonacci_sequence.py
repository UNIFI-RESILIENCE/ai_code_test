To efficiently compute the nth element of the Fib4 sequence without using recursion, we can implement an iterative solution using a sliding window of the last four computed values.

Here is the optimal implementation:

def fib4(n: int):
    """Compute the n-th number in the Fib4 sequence."""
    if n == 0 or n == 1 or n == 3:
        return 0
    if n == 2:
        return 2

    a, b, c, d = 0, 0, 2, 0  # Corresponds to fib4(0), fib4(1), fib4(2), fib4(3)

    for _ in range(4, n + 1):
        next_val = a + b + c + d
        a, b, c, d = b, c, d, next_val

    return d

This code uses constant space and runs in O(n) time, making it optimal for large values of n.

Explanation:
- Initializes values for fib4(0) to fib4(3)
- Iteratively computes each next fib4 value from the previous four
- Avoids recursion entirely

This implementation satisfies all the provided test cases.