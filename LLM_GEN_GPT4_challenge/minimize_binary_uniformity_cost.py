def minimum_cost_to_make_equal(s):
    n = len(s)
    
    # Initialize the array to store minimum cost to make all characters equal to the left of each index
    left_cost = [0] * n
    cost = 0
    flip = 0  # Number of flips applied (parity)

    # Traverse from left to right to calculate cumulative cost of flipping from index 0 to i
    for i in range(n):
        # Determine actual value of s[i] considering the number of flips
        actual = int(s[i])
        if flip % 2 != 0:
            actual ^= 1  # Simulate the flipping effect

        # If actual is '1', it needs to be flipped to '0'
        if actual == 1:
            cost += i + 1
            flip += 1  # Update the flip count

        left_cost[i] = cost  # Store cost so far to make all from 0 to i equal to '0'

    # Initialize the array to store minimum cost to make all characters equal to the right of each index
    right_cost = [0] * n
    cost = 0
    flip = 0  # Reset flip count for the right side processing

    # Traverse from right to left to calculate cumulative cost of flipping from index i to n-1
    for i in range(n - 1, -1, -1):
        actual = int(s[i])
        if flip % 2 != 0:
            actual ^= 1  # Apply current flip to simulate real value

        # If actual is '1', it needs to be flipped to '0'
        if actual == 1:
            cost += n - i
            flip += 1  # Update the flip count

        right_cost[i] = cost  # Store cost so far to make all from i to n-1 equal to '0'

    # Initialize result with minimum of converting whole string to all '0's or all '1's
    result = min(left_cost[-1], right_cost[0])

    # Try all split points where characters before i are made same and after i are made same
    for i in range(n - 1):
        result = min(result, left_cost[i] + right_cost[i + 1])

    return result