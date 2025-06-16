def string_sequence(n: int) -> str:
    # Generate a sequence of integers from 0 to n (inclusive)
    # Convert each integer to a string and join them with a space separator
    return ' '.join(str(i) for i in range(n + 1))