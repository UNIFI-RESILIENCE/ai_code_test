import sys
MOD = 998244353

def solve():
    N, K = map(int, sys.stdin.readline().split())
    S = sys.stdin.readline().strip()
    
    # Precompute the DP table
    # dp[mask][last_K_chars] where mask is a bitmask representing constraints from previous positions
    # Since K is up to 10, last_K_chars can be represented as a bitmask (0=A, 1=B)
    
    # Initialize DP
    # We'll use a dictionary to represent the current state to save space
    dp = {}
    # The initial state is empty (no characters processed yet)
    # mask represents constraints up to the first 0 characters (empty)
    # The initial last K characters are also empty (but since no characters are processed, it's handled as 0)
    # The initial count is 1 (empty string)
    dp[(0, 0)] = 1
    
    for i in range(N):
        new_dp = {}
        c = S[i]
        for (mask, last), cnt in dp.items():
            possible_chars = []
            if c == '?':
                possible_chars = ['A', 'B']
            else:
                possible_chars = [c]
            
            for ch in possible_chars:
                new_last = ((last << 1) | (1 if ch == 'B' else 0)) & ((1 << K) - 1)
                new_mask = mask
                # Check if adding 'ch' creates any forbidden palindromes
                # The new_last has K bits, but we need to check all lengths up to K
                # We need to check if any substring of length >=2 and <=K in the new_last is a palindrome
                # But since we process character by character, we only need to check the new palindromes ending at the current position
                ok = True
                # Check all lengths l from 2 to min(K, current_length +1)
                current_length = (i + 1)
                max_l = min(K, current_length)
                for l in range(2, max_l + 1):
                    # Extract the substring of length l ending at current position
                    # The substring is represented by the last l bits of new_last
                    substr = (new_last >> (K - l)) & ((1 << l) - 1)
                    # Check if substr is a palindrome
                    # A number is a palindrome if its bits mirror
                    is_palindrome = True
                    for j in range(l // 2):
                        left_bit = (substr >> (l - 1 - j)) & 1
                        right_bit = (substr >> j) & 1
                        if left_bit != right_bit:
                            is_palindrome = False
                            break
                    if is_palindrome:
                        ok = False
                        break
                if not ok:
                    continue
                # Update the mask: the mask is used to ensure that the constraints from previous positions are not violated
                # The mask is a bitmask where each bit represents whether a certain position has been constrained
                # For now, we can ignore the mask and proceed
                # The new state is (new_mask, new_last)
                key = (new_mask, new_last)
                new_dp[key] = (new_dp.get(key, 0) + cnt) % MOD
        dp = new_dp
        if not dp:
            break
    
    total = 0
    for (mask, last), cnt in dp.items():
        total = (total + cnt) % MOD
    print(total)

solve()