def is_palindrome_basic(s):
    """
    Check if a string is a palindrome (case-sensitive).
    
    Args:
        s (str): The string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    return s == s[::-1]
```

## Case-Insensitive Version

```python
def is_palindrome(s):
    """
    Check if a string is a palindrome (case-insensitive).
    
    Args:
        s (str): The string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    s = s.lower()
    return s == s[::-1]
```

## Advanced Version (Ignores Spaces and Punctuation)

```python
def is_palindrome_advanced(s):
    """
    Check if a string is a palindrome, ignoring spaces, punctuation, and case.
    
    Args:
        s (str): The string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Keep only alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]
```

## Two-Pointer Approach (More Memory Efficient)

```python
def is_palindrome_two_pointer(s):
    """
    Check if a string is a palindrome using two pointers (memory efficient).
    
    Args:
        s (str): The string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Clean the string
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    left = 0
    right = len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True
```

## Example Usage

```python
# Test the functions
test_strings = [
    "racecar",           # True
    "A man a plan a canal Panama",  # True
    "race a car",        # False
    "hello",             # False
    "Madam",             # True
    "Was it a rat I saw?",  # True
    "",                  # True (empty string)
    "a"                  # True (single character)
]

print("Testing palindrome functions:")
for test in test_strings:
    result = is_palindrome_advanced(test)
    print(f"'{test}' -> {result}")
```

## Output:
```
Testing palindrome functions:
'racecar' -> True
'A man a plan a canal Panama' -> True
'race a car' -> False
'hello' -> False
'Madam' -> True
'Was it a rat I saw?' -> True
'' -> True
'a' -> True