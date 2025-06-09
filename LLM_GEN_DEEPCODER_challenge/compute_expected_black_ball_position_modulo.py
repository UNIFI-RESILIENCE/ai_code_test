import sys

def solve():
    N, K = map(int, sys.stdin.readline().split())
    MOD = 998244353
    
    # The transition probabilities can be modeled with a Markov chain
    # The black ball starts at position 1 (0-based or 1-based doesn't matter as we adjust later)
    # For each step, the probability that the black ball moves is (N-1)/N * 2/(N-1) = 2/N
    # Because:
    #   Probability a != b is (N-1)/N.
    #   Given a != b, the probability that either a or b is the current position of black is 2*(N-1)/(N(N-1)) = 2/N
    # So for each swap, regardless of the current position, the probability to move is 2/N
    # Then, the probability to not move is (N-2)/N

    inv_N = pow(N, MOD-2, MOD)  # modular inverse of N
    
    # Probability to move during one operation: move_p = 2/N
    move_p = 2 * inv_N % MOD
    stay_p = (1 - move_p) % MOD
    
    # We need to model the expected position after K steps
    # Let's model E[k] = (Expected position after k steps)
    # The initial position is 0 (assuming 0-based for easier computation)
    # E[k+1] = stay_p * E[k] + move_p * ( (E[k] * (N-1) + N*(N-1)/2 ) / (N-1) )
    # Let's break this down:
    #   After staying, the contribution is E[k]
    #   After moving, the new expected position is the average of all other positions (since when swapped, it goes to a random other position)
    #   The average of all other positions is (sum_{i=0 to N-1} i - current_pos)/(N-1)
    #   But since we model expectation, we use expectation as current_pos is E[k] in the former step
    # So ((N-1)*N/2 - E[k])/(N-1) = ( (N)/2 - E[k]/(N-1) )
    
    # So, E[k+1] = stay_p * E[k] + move_p * (N-1)/2 - (move_p)/(N-1)*E[k]
    # Combining terms with E[k]: (stay_p - move_p/(N-1)) = ( (N-2)/N - 2/(N(N-1)) )
    # Simplify: ( (N-2)(N-1) - 2 ) / (N(N-1)) )
    # (N² -3N + 2 -2) / (N(N-1)) = (N² - 3N)/(N(N-1)) = N(N-3)/(N(N-1)) = (N-3)/(N-1)
    
    # Move_p is 2/N, so move_p * (N-1)/2 = (2/N)*(N-1)/2 = (N-1)/N
    
    # Re-formulating:
    # E[k+1] = [(N-3)/(N-1)] * E[k] + (N-1)/N
    
    # But it's easier to handle in the code:
    coef1 = (1 - (2 * inv_N % MOD)) % MOD  # (N-2)/N
    # The second term when moving is (sum of average other positions)
    # Average other positions when E[k] is expected current position: (total sum - E[k])/(N-1)
    total_sum = (N - 1) * N // 2 % MOD  # sum of 0..N-1 mod MOD (assuming 0-based positions)
    inv_N_minus_1 = pow(N - 1, MOD - 2, MOD) if N > 1 else 0
    
    E = 0  # initial position is 0 (0-based)
    for _ in range(K):
        # When moving, expected new position is (total_sum - E) * inv_N_minus_1 mod MOD
        term_move = (total_sum - E) * inv_N_minus_1 % MOD if N > 1 else 0
        E = (stay_p * E + move_p * term_move) % MOD
    
    # The expected position is E in 0-based, output E+1 mod MOD
    ans = (E + 1) % MOD
    print(ans)

solve()