def second_largest(numbers):
    if len(numbers) < 2:
        raise ValueError("List must contain at least two unique elements")

    # Convert the list to a set to remove duplicates and then back to a list
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        raise ValueError("List must contain at least two unique elements")

    # Sort the list in descending order
    unique_numbers.sort(reverse=True)

    # Return the second largest number
    return unique_numbers[1]

# Example usage:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(second_largest(numbers))  # Output: 6