import math

def truncate_number(number: float) -> float:
    # Decompose the number into its integer and decimal parts
    integer_part = math.floor(number)  # Get the largest integer smaller than the number
    decimal_part = number - integer_part  # Subtract the integer part from the original number to get the decimal part
    
    return decimal_part  # Return the decimal part of the number

# Metadata dictionary containing information about the author and dataset
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

# Function to check the correctness of the truncate_number function
def check(candidate):
    assert candidate(3.5) == 0.5, "Test case 1 failed"
    assert abs(candidate(1.33) - 0.33) < 1e-6, "Test case 2 failed"
    assert abs(candidate(123.456) - 0.456) < 1e-6, "Test case 3 failed"

# Uncomment the line below to run the check function with truncate_number as the candidate
# check(truncate_number)