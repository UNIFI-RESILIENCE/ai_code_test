MOD = 998244353

def modinv(x):
    """Compute the modular inverse of x modulo MOD using Fermat's Little Theorem."""
    return pow(x, MOD - 2, MOD)

def solve():
    import sys
    input = sys.stdin.read
    N, K = map(int, input().split())

    # Initialize probability distribution:
    # dp[i] is the probability that the black ball is at position i (0-based index)
    dp = [0] * N
    dp[0] = 1  # The black ball starts at position 0 (1st position)

    # Total number of uniformly random operations C = N * (N - 1)
    total_choices = N * (N - 1) % MOD
    inv_total_choices = modinv(total_choices)

    for _ in range(K):
        # Create a new accumulator for the next round
        new_dp = [0] * N

        # Sum of probabilities (for calculating the transitions later)
        total_prob = sum(dp) % MOD

        # Precompute total transitions into each position
        suffix_sum = [0] * (N + 1)

        # Accumulate suffix sum for fast range summing
        # Going to use this to compute the sum over j != i of dp[j]
        for i in range(N - 1, -1, -1):
            suffix_sum[i] = (dp[i] + suffix_sum[i + 1]) % MOD

        for i in range(N):
            # Count how many (a, b) with a != b result in position i getting the black ball

            # For each position i, the probability that it gains the black ball is:
            # sum over j != i of (dp[j] * 2) * (1 / (N * (N - 1)))
            # Explanation:
            # For any j ≠ i, we can have:
            # - (a = i, b = j) OR (a = j, b = i) --> 2 ways out of N*(N-1) total

            # sum_dp_except_i = total_prob - dp[i]
            gain = ((total_prob - dp[i]) * 2 * inv_total_choices) % MOD
            
            # Stay case:
            # There are (N - 1) choices for a != b where i is not involved,
            # which causes the black ball to stay at its current position.
            # So, probability of staying is:
            # p_stay = dp[i] * (number of such swaps) / total events
            # number of such swaps = N * (N - 1) - 2 * (N - 1)
            no_swap_count = (N * (N - 1) - 2 * (N - 1)) % MOD
            stay = (dp[i] * no_swap_count * inv_total_choices) % MOD

            new_dp[i] = (gain + stay) % MOD

        dp = new_dp

    # Calculate the expected value:
    # Expected position is sum over i of dp[i] * (i + 1)
    expected = 0
    for i in range(N):
        expected = (expected + dp[i] * (i + 1)) % MOD

    # Print the expected value modulo MOD
    print(expected)