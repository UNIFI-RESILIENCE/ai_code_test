from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) of a list of numbers.
    
    Args:
        numbers: List of floats representing the dataset.
    
    Returns:
        float: The Mean Absolute Deviation of the dataset.
    
    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the mean of the dataset
    mean = sum(numbers) / len(numbers)
    
    # Calculate the sum of absolute differences from the mean
    absolute_differences = [abs(x - mean) for x in numbers]
    
    # Compute the average of absolute differences (MAD)
    mad = sum(absolute_differences) / len(absolute_differences)
    
    return mad