def is_prime(num):
    """
    Check if a number is prime.
    
    Args:
        num (int): The number to be checked.
        
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Negative numbers and 0 are not prime
    if num < 2:
        return False
    
    # 2 is the only even prime number
    if num == 2:
        return True
    
    # All other even numbers are not prime
    if num % 2 == 0:
        return False
    
    # Check for odd numbers up to sqrt(num)
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    
    return True
```

Here's how the function works:

1. First, we check if the input number `num` is less than 2. If it is, we return `False` because negative numbers and 0 are not prime.
2. Next, we check if `num` is 2, which is the only even prime number. If it is, we return `True`.
3. Then, we check if `num` is divisible by 2 (i.e., even). If it is, we return `False` because all other even numbers are not prime.
4. If `num` is an odd number, we loop through all odd numbers from 3 up to the square root of `num` (inclusive). If we find any number that divides `num`, we return `False` because `num` is not prime.
5. If we don't find any factor of `num` in the loop, we return `True` because `num` is prime.

Here's an example of how to use the `is_prime` function:

```python
print(is_prime(7))  # True
print(is_prime(10))  # False
print(is_prime(17))  # True
print(is_prime(0))  # False
print(is_prime(-3))  # False
```

This will output:

```
True
False
True
False
False