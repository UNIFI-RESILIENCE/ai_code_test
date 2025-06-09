from sys import stdin
import sys
input = stdin.readline

MOD = 998244353

def is_palindrome(s):
    return s == s[::-1]

def main():
    N, K = map(int, input().split())
    S = input().strip()

    # Precompute all palindromes of length K using 'A' and 'B'
    palindromes = set()
    from itertools import product
    for comb in product('AB', repeat=K):
        comb_str = ''.join(comb)
        if is_palindrome(comb_str):
            palindromes.add(comb_str)

    # dp[i][mask]: number of valid strings up to position i-1 ending with the last (K-1) characters as `mask`
    # mask is a string of length <= K-1
    from collections import defaultdict

    dp = defaultdict(int)
    dp[""] = 1  # base case, empty string has 1 way

    for idx in range(N):
        next_dp = defaultdict(int)
        ch = S[idx]
        options = ['A', 'B'] if ch == '?' else [ch]

        for mask, count in dp.items():
            for c in options:
                new_mask = (mask + c)[- (K - 1):]  # keep only last K-1 characters
                if len(mask) == K - 1:
                    candidate = mask + c
                    if candidate in palindromes:
                        continue  # skip if this completes a bad (palindromic) substring of length K
                next_dp[new_mask] = (next_dp[new_mask] + count) % MOD

        dp = next_dp

    result = sum(dp.values()) % MOD
    print(result)

if __name__ == "__main__":
    sys.setrecursionlimit(1 << 25)
    main()