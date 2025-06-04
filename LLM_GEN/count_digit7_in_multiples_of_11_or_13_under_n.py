Here's the optimal implementation of the fizz_buzz function based on the provided description:

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n 
    which are divisible by 11 or 13.
    """
    count = 0
    for x in range(n):
        if x % 11 == 0 or x % 13 == 0:
            count += str(x).count('7')
    return count

This function:

1. Iterates from 0 to n - 1.
2. Checks whether each number is divisible by 11 or 13.
3. Converts qualifying numbers to a string and counts the number of '7' digits.
4. Accumulates the total count and returns it.

This is both simple and efficient for values of n up to and beyond 100,000.