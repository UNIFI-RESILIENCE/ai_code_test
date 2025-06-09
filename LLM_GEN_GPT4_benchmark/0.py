from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # First, sort the list to bring close elements next to each other
    numbers.sort()

    # Iterate through adjacent elements and check if any two numbers
    # have a difference less than the threshold
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < threshold:
            return True  # Found a pair of elements with distance less than threshold

    # If no such pair is found, return False
    return False


print(has_close_elements([6.0, 4.5,23.4,52.3],100.2))