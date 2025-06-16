def fizz_buzz(n: int) -> int:
    # Initialize a counter to keep track of the number of times the digit 7 appears
    count_seven = 0
    
    # Iterate over each number from 1 up to (but not including) n
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string and count occurrences of '7'
            count_seven += str(i).count('7')
    
    # Return the total count of the digit 7 found in numbers divisible by 11 or 13
    return count_seven

# Example usage:
# print(fizz_buzz(50))  # Output: 0
# print(fizz_buzz(78))  # Output: 2
# print(fizz_buzz(79))  # Output: 3