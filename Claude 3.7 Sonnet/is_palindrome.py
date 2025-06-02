def is_palindrome(string):
    # Convert the string to lowercase and remove non-alphanumeric characters
    cleaned_string = ''.join(char for char in string.lower() if char.isalnum())

    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]
```

Here's how the `is_palindrome()` function works:

1. The function takes a string as input.
2. It creates a new string `cleaned_string` by converting the input string to lowercase and removing all non-alphanumeric characters (i.e., characters that are not letters or digits) using a list comprehension and the `isalnum()` method.
3. It checks if `cleaned_string` is equal to its reverse (`cleaned_string[::-1]`). The slice notation `[::-1]` creates a new string that is the reverse of the original string.
4. The function returns `True` if `cleaned_string` is equal to its reverse (i.e., if it's a palindrome), and `False` otherwise.

Here are some examples of how to use the `is_palindrome()` function:

```python
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("Hello, World!"))  # Output: False
print(is_palindrome("Madam, I'm Adam"))  # Output: True