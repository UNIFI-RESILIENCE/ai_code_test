from functools import lru_cache

def paintWalls(cost, time):
    n = len(cost)

    # Use memoization to cache results of subproblems
    @lru_cache(None)
    def dp(i, t_free):
        # Base case: all walls painted
        if i == n:
            return 0 if t_free >= 0 else float('inf')

        # Option 1: Use paid painter for wall i
        # Increases available time for free painter by time[i],
        # and adds cost[i] to the total cost
        option1 = cost[i] + dp(i + 1, t_free + time[i])

        # Option 2: Use free painter for wall i
        # Only allowed if we have free time units available
        option2 = float('inf')
        if t_free > 0:
            option2 = dp(i + 1, t_free - 1)

        # Return the minimum of both options
        return min(option1, option2)

    # Start from the first wall with zero free time available
    return dp(0, 0)