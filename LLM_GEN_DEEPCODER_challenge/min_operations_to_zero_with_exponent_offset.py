def make_num1_zero(num1: int, num2: int) -> int:
    """
    Calculates the minimum number of operations to reduce num1 to 0 by subtracting (2^i + num2) in each step.
    Returns -1 if it's impossible.
    
    Approach:
    1. The key observation is that each operation subtracts a value of the form (2^i + num2).
    2. The problem reduces to representing num1 as a sum of such terms with minimal operations.
    3. For each possible number of operations k, we check if num1 - k*num2 can be expressed as the sum of k powers of 2.
    4. The powers of 2 can be same or different, but the total count must be exactly k.
    5. We iterate over possible k values (from 0 to 60, since 2^60 is large enough to cover 1e9).
    
    Args:
        num1: The initial number to reduce to 0.
        num2: The fixed number added to 2^i in each operation.
    
    Returns:
        The minimal operations needed or -1 if impossible.
    """
    for k in range(61):
        remaining = num1 - k * num2
        if remaining < 0:
            continue
        # Check if remaining can be represented as sum of k powers of 2
        # The minimal binary representation has number of 1s <= k and sum of bits == k
        if bin(remaining).count('1') <= k and remaining >= k:
            return k
    return -1