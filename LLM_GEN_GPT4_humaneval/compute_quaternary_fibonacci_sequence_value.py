def fib4(n: int):
    # Handle base cases directly
    if n == 0 or n == 1 or n == 3:
        return 0
    elif n == 2:
        return 2

    # Initialize the first four values of the sequence
    a, b, c, d = 0, 0, 2, 0

    # Compute the sequence iteratively up to n
    for i in range(4, n + 1):
        current = a + b + c + d
        # Shift the window for the next iteration
        a, b, c, d = b, c, d, current

    return d