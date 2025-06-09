def punishment_number(n):
    # Helper function to check if we can split square_str such that parts sum to target
    def can_partition(square_str, target):
        # Use DFS with memoization
        memo = {}

        def dfs(index, current_sum):
            # If we've reached the end of the string
            if index == len(square_str):
                return current_sum == target

            key = (index, current_sum)
            if key in memo:
                return memo[key]

            # Try all possible splits starting at index
            for j in range(index + 1, len(square_str) + 1):
                part = square_str[index:j]
                num = int(part)

                if dfs(j, current_sum + num):
                    memo[key] = True
                    return True

            memo[key] = False
            return False

        return dfs(0, 0)

    result = 0

    # Iterate through all integers from 1 to n
    for i in range(1, n + 1):
        square = i * i
        square_str = str(square)

        # Check if square_str can be partitioned to sum to i
        if can_partition(square_str, i):
            result += square

    return result