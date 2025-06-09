def paintWalls(cost, time):
    n = len(cost)
    # dp[i][j] represents the minimum cost to paint 'i' walls with 'j' extra walls that can be painted by the free painter
    # Initialize DP table with infinity, size based on constraints (max time is 500 per wall, so max j is 500)
    max_time = 500
    dp = [[float('inf')] * (2 * max_time + 1) for _ in range(n + 1)]
    dp[0][max_time] = 0  # Base case: 0 walls, 0 extra time
    
    for i in range(n):
        current_cost = cost[i]
        current_time = time[i]
        for j in range(-max_time, max_time + 1):
            if dp[i][j + max_time] == float('inf'):
                continue
            # Option 1: Don't take the paid painter for wall i
            # Free painter can paint this wall if j > 0 (i.e., there's extra time from paid painters)
            if j - 1 >= -max_time:
                new_j = j - 1
                if new_j + max_time >= 0 and new_j + max_time <= 2 * max_time:
                    if dp[i + 1][new_j + max_time] > dp[i][j + max_time]:
                        dp[i + 1][new_j + max_time] = dp[i][j + max_time]
            # Option 2: Take the paid painter for wall i
            # This adds current_time to the available free painter time
            new_j = j + current_time
            if new_j + max_time >= 0 and new_j + max_time <= 2 * max_time:
                if dp[i + 1][new_j + max_time] > dp[i][j + max_time] + current_cost:
                    dp[i + 1][new_j + max_time] = dp[i][j + max_time] + current_cost
    
    # The answer is the minimum cost for n walls where j >= 0 (enough free time to cover remaining walls)
    min_cost = float('inf')
    for j in range(0, max_time + 1):
        if dp[n][j + max_time] < min_cost:
            min_cost = dp[n][j + max_time]
    return min_cost