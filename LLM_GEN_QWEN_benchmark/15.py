def string_sequence(n: int) -> str:
    # Use a generator expression to create a sequence of numbers from 0 to n
    # Convert each number to a string and join them with a space delimiter
    return ' '.join(str(i) for i in range(n + 1))

# Example usage:
# result = string_sequence(5)
# print(result)  # Output: '0 1 2 3 4 5'