def minCost(nums, x):
    n = len(nums)
    
    # Initialize a list of lists to store the minimum cost to collect each type of chocolate
    # Each inner list will store the minimum cost to collect a particular type after a certain number of shifts
    min_cost_to_collect = [[float('inf')] * n for _ in range(n)]
    
    # Iterate over each type of chocolate to find the minimum cost to collect it after k shifts
    for chocolate_type in range(n):
        # The initial cost to collect the i^th type chocolate is nums[i]
        min_cost_to_collect[chocolate_type][0] = nums[chocolate_type]
        for shift in range(1, n):
            # The chocolate type after shift operations is (chocolate_type + shift) % n
            new_position = (chocolate_type + shift) % n
            # Update the minimum cost to collect this chocolate type after the current shift
            min_cost_to_collect[chocolate_type][shift] = min(
                min_cost_to_collect[chocolate_type][shift - 1],
                nums[new_position]
            )
    
    # Initialize the minimum total cost to a large number
    min_total_cost = float('inf')
    
    # Iterate over all possible number of shift operations (from 0 to n-1)
    for shift in range(n):
        # Calculate the total cost to collect all types of chocolates after the current shift
        current_total_cost = sum(min_cost_to_collect[chocolate_type][shift] for chocolate_type in range(n))
        # Add the cost of performing the shift operation 'shift' times
        current_total_cost += shift * x
        # Update the minimum total cost found so far
        min_total_cost = min(min_total_cost, current_total_cost)
    
    return min_total_cost

# Test cases
print(minCost([20, 1, 15], 5))  # Output: 13
print(minCost([1, 2, 3], 4))    # Output: 6