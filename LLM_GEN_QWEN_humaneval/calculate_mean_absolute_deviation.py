from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the mean of the numbers
    mean_value = statistics.mean(numbers)
    
    # Compute the absolute deviations from the mean
    absolute_deviations = [abs(x - mean_value) for x in numbers]
    
    # Calculate the mean of these absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0 / 3.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0 / 5.0) < 1e-6

# Uncomment the line below to run the checks
# check(mean_absolute_deviation)