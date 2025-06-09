def punishment_number(n):
    """
    Calculate the punishment number of n, which is the sum of squares of all integers i (1 <= i <= n)
    such that the decimal representation of i^2 can be partitioned into contiguous substrings that sum to i.
    
    Args:
    n (int): The upper bound for integers to consider.
    
    Returns:
    int: The punishment number of n.
    """
    total = 0
    
    for i in range(1, n + 1):
        square = i * i
        square_str = str(square)
        if can_partition(square_str, i):
            total += square
    return total

def can_partition(s, target):
    """
    Helper function to check if the string s can be partitioned into contiguous substrings
    that sum up to the target.
    
    Args:
    s (str): The string representation of the square of a number.
    target (int): The original number to check partitions against.
    
    Returns:
    bool: True if such a partition exists, False otherwise.
    """
    if not s:
        return target == 0
    
    for i in range(1, len(s) + 1):
        current = int(s[:i])
        remaining = s[i:]
        if can_partition(remaining, target - current):
            return True
    return False