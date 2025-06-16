def fib4(n: int):
    # Handle base cases as per the sequence definition
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    # Initialize the first four elements of the sequence
    a, b, c, d = 0, 0, 2, 0  # Correspond to fib4(0), fib4(1), fib4(2), fib4(3)

    # Iteratively compute fib4 sequence from index 4 to n
    for i in range(4, n + 1):
        next_val = a + b + c + d  # Compute next value based on previous 4 elements
        a, b, c, d = b, c, d, next_val  # Update tracking variables

    return d  # d holds the value of fib4(n) after the loop completes