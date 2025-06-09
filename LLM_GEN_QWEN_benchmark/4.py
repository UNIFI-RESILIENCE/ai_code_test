from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Compute the sum of absolute deviations from the mean
    total_absolute_deviation = sum(abs(x - mean) for x in numbers)
    
    # Calculate the mean of the absolute deviations
    mad = total_absolute_deviation / len(numbers)
    
    return mad

# Example usage
if __name__ == "__main__":
    data = [1.0, 2.0, 3.0, 4.0]
    result = mean_absolute_deviation(data)
    print(f"Mean Absolute Deviation: {result}")  # Output: Mean Absolute Deviation: 1.0