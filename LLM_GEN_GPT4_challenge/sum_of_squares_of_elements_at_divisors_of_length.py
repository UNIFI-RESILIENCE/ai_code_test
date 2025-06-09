def sum_of_squares_of_special_elements(nums):
    n = len(nums)
    total = 0

    # Iterate through each index from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Check if the index divides n (i.e., is a divisor of n)
        if n % i == 0:
            # Subtract 1 for 0-based index access and add square of nums[i-1] to total
            total += nums[i - 1] ** 2

    return total
```