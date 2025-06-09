from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return 0.0  # Return 0.0 for empty list as there is no deviation

    # Compute the mean (average) of the numbers
    mean = sum(numbers) / len(numbers)

    # Compute the sum of absolute differences from the mean
    total_absolute_deviation = sum(abs(x - mean) for x in numbers)

    # Compute and return the mean absolute deviation
    mad = total_absolute_deviation / len(numbers)
    return mad