def minimumSum(n, k):
    result = []
    num = 1
    used = set()

    while len(result) < n:
        # Skip numbers that would create a pair summing to k
        if k - num not in used:
            result.append(num)
            used.add(num)
        num += 1

    return sum(result)

# Example usage:
# print(minimumSum(5, 4))  # Output: 18
# print(minimumSum(2, 6))  # Output: 3