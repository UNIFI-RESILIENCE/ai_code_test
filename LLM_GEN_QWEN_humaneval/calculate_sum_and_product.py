from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # Initialize sum to 0 and product to 1 as per the problem statement
    total_sum = 0
    total_product = 1

    # Iterate through each number in the list
    for number in numbers:
        # Add the current number to the total sum
        total_sum += number
        # Multiply the current number to the total product
        total_product *= number

    # Return a tuple consisting of the total sum and total product
    return total_sum, total_product


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    # Test cases to validate the correctness of the sum_product function
    assert candidate([]) == (0, 1), "Test with an empty list failed"
    assert candidate([1, 1, 1]) == (3, 1), "Test with a list of ones failed"
    assert candidate([100, 0]) == (100, 0), "Test with a list containing zero failed"
    assert candidate([3, 5, 7]) == (15, 105), "Test with a list of positive integers failed"
    assert candidate([10]) == (10, 10), "Test with a single-element list failed"

# Call the check function to run the test cases
check(sum_product)