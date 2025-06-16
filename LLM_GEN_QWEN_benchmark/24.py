def largest_divisor(n: int) -> int:
    # Start checking from n-1 down to 1
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i  # Return the first (largest) divisor found