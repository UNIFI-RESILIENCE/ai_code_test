def second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements for a second largest

    # Convert the list to a set to remove duplicates, then back to a list
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None  # Not enough unique elements for a second largest

    # Sort the list in descending order
    unique_numbers.sort(reverse=True)

    # Return the second element
    return unique_numbers[1]

# Example usage:
numbers = [4, 1, 7, 3, 7, 8, 8, 5]
print(second_largest(numbers))  # Output: 7
```

This function first checks if the list has fewer than two elements, in which case it returns `None` because a second largest number doesn't exist. Then, it removes duplicates by converting the list to a set and back to a list. If there are still fewer than two unique elements, it again returns `None`. Otherwise, it sorts the list in descending order and returns the second element.

Alternatively, you can achieve the same result without sorting the entire list, which can be more efficient:

```python
def second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements for a second largest

    # Initialize the two largest numbers
    first, second = float('-inf'), float('-inf')

    for number in numbers:
        if number > first:
            # Update both first and second
            first, second = number, first
        elif first > number > second:
            # Update only second
            second = number

    # Check if a second largest number was found
    return second if second != float('-inf') else None

# Example usage:
numbers = [4, 1, 7, 3, 7, 8, 8, 5]
print(second_largest(numbers))  # Output: 7