from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    # List to store the rolling maximums
    result = []

    # Variable to keep track of the current maximum
    current_max = float('-inf')

    # Iterate over each number in the input list
    for num in numbers:
        # Update current_max if current number is greater
        if num > current_max:
            current_max = num
        # Append the current maximum to the result list
        result.append(current_max)

    return result

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([4, 3, 2, 1]) == [4, 4, 4, 4]
    assert candidate([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]