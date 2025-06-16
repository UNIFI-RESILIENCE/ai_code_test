from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    # Initialize an empty list to store the rolling maximums
    result = []

    # Initialize the current maximum to negative infinity
    current_max = float('-inf')

    # Iterate through the input list
    for num in numbers:
        # Update current_max if the current number is greater
        if num > current_max:
            current_max = num
        # Append the current maximum to the result list
        result.append(current_max)

    return result