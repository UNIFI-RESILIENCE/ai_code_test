from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return 0.0  # Return 0.0 for empty input to handle edge case

    # Compute the mean of the list
    mean = sum(numbers) / len(numbers)

    # Compute the absolute deviations from the mean
    abs_deviations = [abs(x - mean) for x in numbers]

    # Return the average of the absolute deviations
    return sum(abs_deviations) / len(numbers)

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):
    # Mean = 2.0; deviations = [1.0, 0.0, 1.0]; MAD = (1+0+1)/3 = 0.666...
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0 / 3.0) < 1e-6

    # Mean = 2.5; deviations = [1.5, 0.5, 0.5, 1.5]; MAD = (1.5+0.5+0.5+1.5)/4 = 1.0
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6

    # Mean = 3.0; deviations = [2.0, 1.0, 0.0, 1.0, 2.0]; MAD = 6/5 = 1.2
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0 / 5.0) < 1e-6