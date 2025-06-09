from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the sum of absolute differences from the mean
    absolute_differences = [abs(x - mean) for x in numbers]
    
    # Return the average of absolute differences (MAD)
    return sum(absolute_differences) / len(numbers)


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6