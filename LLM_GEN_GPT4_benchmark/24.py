def largest_divisor(n: int) -> int:
    # Iterate from n // 2 down to 1 to find the largest proper divisor
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            # Return the first (largest) divisor found
            return i
    # Fallback case; should not occur for input n > 1
    return 1