def fizz_buzz(n: int) -> int:
    count = 0
    for i in range(n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Count occurrences of digit '7' in the current number
            count += str(i).count('7')
    return count