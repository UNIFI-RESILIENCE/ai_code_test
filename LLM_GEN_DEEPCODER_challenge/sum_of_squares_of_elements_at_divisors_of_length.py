def sum_of_squares(nums):
    """
    Calculate the sum of the squares of all special elements in the array.
    
    Args:
    nums (List[int]): A 1-indexed integer array.
    
    Returns:
    int: The sum of the squares of all special elements.
    """
    n = len(nums)
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            # Current index is special, add its square to the total
            total += nums[i - 1] ** 2  # Convert to 0-based index for accessing the list
    return total