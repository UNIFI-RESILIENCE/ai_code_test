def fib4(n: int) -> int:
    # Base cases for the sequence
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    # Initialize the first four elements of the sequence
    fib4_values = [0, 0, 2, 0]

    # Iterate from the 4th index up to n to compute the sequence
    for i in range(4, n + 1):
        # Calculate the next value in the sequence based on the last four values
        next_value = fib4_values[0] + fib4_values[1] + fib4_values[2] + fib4_values[3]
        
        # Update the list to hold the last four values
        fib4_values[0] = fib4_values[1]
        fib4_values[1] = fib4_values[2]
        fib4_values[2] = fib4_values[3]
        fib4_values[3] = next_value

    # Return the n-th element of the sequence
    return fib4_values[3]

# Example usage
if __name__ == "__main__":
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14