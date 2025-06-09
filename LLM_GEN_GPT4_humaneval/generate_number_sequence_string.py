def string_sequence(n: int) -> str:
    # Generate a sequence of numbers from 0 to n (inclusive)
    # Convert each number to a string
    # Join the string representations with a space delimiter
    return ' '.join(str(i) for i in range(n + 1))