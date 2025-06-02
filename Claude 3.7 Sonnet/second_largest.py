def find_second_largest(numbers):
    # Check if the list has at least two elements
    if len(numbers) < 2:
        return None

    # Find the largest number
    largest = max(numbers)

    # Initialize the second largest number to the smallest possible value
    second_largest = float('-inf')

    # Iterate through the list and find the second largest number
    for num in numbers:
        if num != largest and num > second_largest:
            second_largest = num

    # If there is no second largest number (all elements are the same), return None
    if second_largest == float('-inf'):
        return None

    return second_largest
```

Here's how the `find_second_largest` function works:

1. First, it checks if the list has at least two elements. If not, it returns `None` because there can't be a second largest number.
2. If the list has two or more elements, it finds the largest number using the `max` function.
3. It initializes the `second_largest` variable to the smallest possible value (`float('-inf')`).
4. It iterates through the list and updates the `second_largest` variable with any number that is greater than the current `second_largest` and not equal to the `largest` number.
5. If all elements in the list are the same, `second_largest` will remain `float('-inf')`, and the function returns `None`.
6. Otherwise, it returns the `second_largest` number.

You can use this function like this:

```python
numbers = [5, 9, 2, 7, 3, 6, 1]
second_largest = find_second_largest(numbers)
print(second_largest)  # Output: 7

numbers = [10, 10, 10, 10]
second_largest = find_second_largest(numbers)
print(second_largest)  # Output: None