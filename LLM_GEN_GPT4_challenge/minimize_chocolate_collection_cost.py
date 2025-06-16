def min_cost(nums, x):
    n = len(nums)
    res = float('inf')

    # Initialize running minimums with the original nums array
    min_costs = nums[:]

    # Try performing 0 to n-1 operations
    for operations in range(n):
        # Calculate total cost after current number of operations
        total = x * operations + sum(min_costs)
        res = min(res, total)

        # Update min_costs for the next operation
        # Each element shifts by one position with wraparound
        for i in range(n):
            min_costs[i] = min(min_costs[i], nums[(i - operations - 1) % n])

    return res