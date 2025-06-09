def minCost(cost, time):
    n = len(cost)
    
    # Initialize dp array with infinity, except dp[0] which is 0
    # dp[i] will represent the minimum cost to paint at least i walls
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # Iterate over each wall
    for i in range(n):
        # Iterate backwards over the dp array to avoid overwriting issues
        for j in range(n, -1, -1):
            # If we use the paid painter on the current wall, then:
            # 1. We incur a cost of cost[i]
            # 2. We paint time[i] walls plus one wall which is the current wall itself
            # Hence, we can paint up to j + time[i] + 1 walls
            if j - (time[i] + 1) >= 0:
                dp[j] = min(dp[j], dp[j - (time[i] + 1)] + cost[i])
                
            # The free painter can paint additional walls if the paid painter is working,
            # but we do not need to update anything here because the dp array considers the
            # maximum walls that can be painted with a certain budget.
            # Therefore, dp[j] is already minimized as much as possible with the current configuration.
    
    # dp[n] will have the minimum cost to paint exactly n walls
    return dp[n]

# Example usage:
cost1 = [1, 2, 3, 2]
time1 = [1, 2, 3, 2]
print(minCost(cost1, time1))  # Output: 3

cost2 = [2, 3, 4, 2]
time2 = [1, 1, 1, 1]
print(minCost(cost2, time2))  # Output: 4