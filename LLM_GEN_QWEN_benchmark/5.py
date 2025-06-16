from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    # If the input list is empty or has only one element, return it as is
    if len(numbers) < 2:
        return numbers

    # Initialize the result list with the first element of the input list
    result = [numbers[0]]

    # Iterate over the input list starting from the second element
    for num in numbers[1:]:
        # Append the delimiter before appending the next number
        result.append(delimiter)
        result.append(num)

    return result

# Example usage:
# print(intersperse([], 4))       # Output: []
# print(intersperse([1, 2, 3], 4)) # Output: [1, 4, 2, 4, 3]