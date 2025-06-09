from typing import List

# Mapping of numberals to their corresponding numeric values
NUMERAL_TO_DIGIT = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

# Reverse mapping of numeric values to numberals
DIGIT_TO_NUMERAL = {v: k for k, v in NUMERAL_TO_DIGIT.items()}

def sort_numbers(numbers: str) -> str:
    # Split the input string into a list of numerals
    numeral_list: List[str] = numbers.split()
    
    # Convert each numeral to its corresponding digit using the mapping
    digit_list: List[int] = [NUMERAL_TO_DIGIT[numeral] for numeral in numeral_list]
    
    # Sort the list of digits
    digit_list.sort()
    
    # Convert the sorted digits back to numerals
    sorted_numeral_list: List[str] = [DIGIT_TO_NUMERAL[digit] for digit in digit_list]
    
    # Join the sorted numerals into a single space-delimited string
    return ' '.join(sorted_numeral_list)

# Metadata for the function
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

# Function to verify the correctness of the `sort_numbers` function
def check(candidate):
    assert candidate('') == '', "Test case with empty string failed"
    assert candidate('three') == 'three', "Test case with single numeral failed"
    assert candidate('three five nine') == 'three five nine', "Sorted case with three numerals failed"
    assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine', "Mixed order test case failed"
    assert candidate('six five four three two one zero') == 'zero one two three four five six', "Reverse order test case failed"

# Example usage
if __name__ == "__main__":
    # Run checks to validate the function
    check(sort_numbers)