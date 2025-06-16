def fizz_buzz(n: int):
    """
    Counts the number of times the digit '7' appears in all integers less than n 
    that are divisible by 11 or 13.
    
    Args:
        n: The upper limit (exclusive) for checking numbers.
    
    Returns:
        The total count of digit '7' occurrences in numbers meeting the criteria.
    
    Examples:
        >>> fizz_buzz(50)
        0
        >>> fizz_buzz(78)
        2
        >>> fizz_buzz(79)
        3
    """
    count = 0
    
    for num in range(1, n):
        # Check if number is divisible by 11 or 13
        if num % 11 == 0 or num % 13 == 0:
            # Convert number to string to count '7's
            count += str(num).count('7')
    
    return count