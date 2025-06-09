def min_cost_to_collect_chocolates(nums, x):
    n = len(nums)
    min_cost = float('inf')
    
    # We can perform rotation up to n times (after that, it cycles)
    for k in range(n):
        total_cost = 0
        # For each chocolate type, find the minimum cost after k rotations
        for i in range(n):
            # The cost is min between:
            # 1. Not rotating: nums[i]
            # 2. Rotating k times: nums[(i - k) % n] + k * x
            # But since we're doing k rotations, we can collect each chocolate after 0..k rotations
            # So for each type, the minimal cost is min(nums[(i - r) % n] + r * x) for r in 0..k
            min_choc_cost = min(
                nums[(i - r) % n] + r * x
                for r in range(k + 1)
            )
            total_cost += min_choc_cost
        min_cost = min(min_cost, total_cost)
    
    return min_cost