MOD = 998244353

def mod_inverse(a, p):
    """Returns the modular inverse of a mod p, using Fermat's little theorem."""
    return pow(a, p - 2, p)

def main():
    import sys
    import sys
    import sys
    
    # Read input
    input = sys.stdin.read().strip().split()
    N = int(input[0])
    K = int(input[1])

    # Base case: if there is only one ball (i.e., N == 1), the black ball remains at position 1.
    if N == 1:
        print(1)
        return

    # Calculate the expected final position of the black ball.
    # This is given by the formula: E(x) = (N + 1) / 2 * (1 - (N - 1) / (N * (N - 1)) ** K)
    # Simplifying, we get: E(x) = (N + 1) / 2 * (1 - (1 / N) ** K)
    # Further simplifying, we get: E(x) = (N + 1) / 2 * (1 - (1 / N) ** K)
    # The expected position can be written as a fraction P/Q, where P = (N+1)/2 * (N**K - 1) and Q = N**K
    # The result needs to be returned modulo 998244353
    numerator = (N + 1) * mod_inverse(2, MOD)
    denominator = pow(N, K, MOD)
    numerator = (numerator * (denominator - 1)) % MOD

    # Compute modular inverse of denominator to get the result
    result = numerator * mod_inverse(denominator, MOD) % MOD
    print(result)

# Entry point of the script
if __name__ == "__main__":
    main()