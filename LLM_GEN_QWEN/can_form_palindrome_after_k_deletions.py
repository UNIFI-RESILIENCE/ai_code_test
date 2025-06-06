import sys
import collections

def can_form_palindrome(n, k, s):
    # Count the frequency of each character in the string
    freq = collections.Counter(s)
    
    # Calculate the number of characters with odd frequency
    odd_count = sum(1 for c in freq if freq[c] % 2 == 1)
    
    # To make a palindrome, we can have at most one character with an odd frequency
    # Therefore, we need to delete enough characters to make at most one of them odd
    # The minimum number of deletions needed is `odd_count - 1` if `odd_count > 1`
    # We need to check if this number (plus some more deletions if necessary) equals `k`
    min_deletions_needed = odd_count - 1 if odd_count > 1 else 0
    
    # If the number of characters to delete is at least the minimum required,
    # and if after deleting `k` characters, we can still rearrange the rest into a palindrome
    if min_deletions_needed <= k:
        return "YES"
    else:
        return "NO"

def main():
    import sys
    input = sys.stdin.read().splitlines()
    
    t_index = 0
    results = []
    
    num_tests = int(input[t_index])
    t_index += 1
    
    for _ in range(num_tests):
        n, k = map(int, input[t_index].split())
        t_index += 1
        s = input[t_index]
        t_index += 1
        results.append(can_form_palindrome(n, k, s))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    # Redirect stdout to output.txt for testing purposes. Remove this when submitting to an online judge
    # with open('output.txt', 'w') as f:
    #    sys.stdout = f
    main()