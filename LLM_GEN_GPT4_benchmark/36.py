def fizz_buzz(n: int):
    # Initialize a counter to keep track of the number of digit '7's found
    count = 0

    # Iterate over each integer less than n
    for i in range(n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Count the occurrences of the digit '7' in the current number
            count += str(i).count('7')

    return count