def longest_substring_without_repeating_chars(s):
    # Create an empty set to store unique characters
    char_set = set()
    
    # Initialize variables
    max_length = 0
    start = 0
    
    # Iterate through the string
    for end in range(len(s)):
        # If the current character is already in the set, remove characters from the start
        # until the current character is removed from the set
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        
        # Add the current character to the set
        char_set.add(s[end])
        
        # Update maximum length
        max_length = max(max_length, len(char_set))
    
    return max_length
```

Here's how the function works:

1. We initialize an empty set `char_set` to store unique characters in the current substring.
2. We initialize two pointers `start` and `end` to represent the start and end of the current substring.
3. We iterate through the string using the `end` pointer.
4. If the current character `s[end]` is already in the `char_set`, we remove characters from the start of the substring until the current character is removed from the set.
5. We add the current character `s[end]` to the `char_set`.
6. We update the `max_length` variable to store the maximum length of the substring without repeating characters.
7. After the loop finishes, we return the `max_length`.

The time complexity of this algorithm is O(n), where n is the length of the input string. This is because we iterate through the string only once, and the operations on the set (adding, removing, and checking for membership) have an amortized constant time complexity.

Here's an example usage:

```python
input_string = "abcabcbb"
print(longest_substring_without_repeating_chars(input_string))  # Output: 3

input_string = "bbbbb"
print(longest_substring_without_repeating_chars(input_string))  # Output: 1

input_string = "pwwkew"
print(longest_substring_without_repeating_chars(input_string))  # Output: 3