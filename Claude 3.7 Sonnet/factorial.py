def factorial(n):
    """
    Recursive function to compute the factorial of a number.
    
    Args:
        n (int): The number for which the factorial is to be calculated.
        
    Returns:
        int: The factorial of the given number.
        
    Raises:
        ValueError: If the input number is negative.
    """
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    # Negative numbers don't have factorial
    elif n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)
```

Here's how the function works:

1. The base case is when `n` is 0, in which case the factorial is defined as 1.
2. If `n` is negative, the function raises a `ValueError` since the factorial is not defined for negative numbers.
3. For all other cases, the function recursively calls itself with `n-1` as the argument and multiplies the result with `n`.

Here are some examples of how to use the function:

```python
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(10)) # Output: 3628800
print(factorial(-3)) # ValueError: Factorial is not defined for negative numbers.