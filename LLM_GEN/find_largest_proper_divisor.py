Here's the optimal implementation for the largest_divisor function:

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i

This function starts checking from n // 2 down to 1 since no number greater than n // 2 (but less than n) can divide n evenly. The first such divisor found in descending order is the largest one.