def can_form_palindrome(n, k, s):
    # Count the frequency of each character in the string
    from collections import Counter
    char_count = Counter(s)
    
    # Count how many characters have an odd frequency
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    
    # For a string to be rearranged into a palindrome:
    # - If the length of the string is even, all characters must have even frequencies
    # - If the length of the string is odd, at most one character can have an odd frequency
    
    # We need to check if after removing k characters, the remaining characters can form a palindrome
    # Removing characters can affect the parity of the counts of characters
    
    # If we can eliminate all odd counts by removing k characters, then it's possible to form a palindrome
    # Removing an odd count character makes it even, and removing an even count character keeps it even
    
    # We need to check if we can reduce the odd count to at most 1 by removing k characters
    # Each removal can reduce the odd count by at most 1 (if we remove one character of an odd count)
    
    # Hence, the condition is: odd_count - k should be less than or equal to 1
    # and k should not exceed n (since we can't remove more characters than present)
    
    if odd_count - k <= 1 and k <= n:
        return "YES"
    else:
        return "NO"

def main():
    import sys
    import sys
    import sys

    import sys
    import sys
    import sys
    import sys
    
    import sys
    import sys
    import sys
    
    import sys
    import sys
    import sys
    
    import sys

    import sys
    import sys
    import sys
    
    import sys
    
    import sys
    
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    
    import sys
    
    import sys
    import sys
    
    import sys
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    import sys
    
    import sys
    import sys
    
    import sys
    import sys
    
    import sys
    
    import sys
    import sys
    
    import sys
    
    import sys
    
    import sys
    import sys
    
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    
    import sys
    import sys
    
    import sys
    
    import sys
    import sys
    
    import sys
    
    import sys
    
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    import sys
    
    input = sys.stdin.read()
    data = input.split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        s = data[index + 2]
        index += 3
        result = can_form_palindrome(n, k, s)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()