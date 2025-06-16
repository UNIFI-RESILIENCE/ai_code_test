def minCostToMakeUniform(s):
    n = len(s)

    # If there is only one character, no operations are needed.
    if n == 1:
        return 0

    # Initialize left and right cost arrays.
    left_cost = [0] * n
    right_cost = [0] * n

    # Calculate minimum cost to make the prefix of length i+1 consistent.
    for i in range(1, n):
        # If the current character is different from the previous one, it requires an inversion.
        if s[i] != s[i - 1]:
            left_cost[i] = left_cost[i - 1] + i
        else:
            left_cost[i] = left_cost[i - 1]

    # Calculate minimum cost to make the suffix of length n-i consistent.
    for i in range(n-2, -1, -1):
        # If the current character is different from the next one, it requires an inversion.
        if s[i] != s[i + 1]:
            right_cost[i] = right_cost[i + 1] + (n - i - 1)
        else:
            right_cost[i] = right_cost[i + 1]

    # Combine the left and right costs to get the minimum cost to make the entire string uniform.
    min_total_cost = float('inf')
    for i in range(n):
        # Cost to make all characters equal choosing the prefix endpoint as i and suffix endpoint as i
        total_cost = left_cost[i] + right_cost[i]
        # Update minimum total cost
        min_total_cost = min(min_total_cost, total_cost)

    return min_total_cost


# Test cases provided in the problem
print(minCostToMakeUniform("0011"))    # Output: 2
print(minCostToMakeUniform("010101"))  # Output: 9