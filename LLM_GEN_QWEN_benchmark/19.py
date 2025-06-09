from typing import List

# Mapping of number words to their numeric values
numeral_map = {
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

# Reverse mapping of numeric values to number words for output conversion
reverse_numeral_map = {v: k for k, v in numeral_map.items()}

def sort_numbers(numbers: str) -> str:
    # Split the input string into individual number words
    number_words = numbers.split()
    
    # Convert number words to their corresponding numeric values
    numeric_values = [numeral_map[word] for word in number_words]
    
    # Sort the numeric values
    sorted_numeric_values = sorted(numeric_values)
    
    # Convert the sorted numeric values back to number words
    sorted_number_words = [reverse_numeral_map[value] for value in sorted_numeric_values]
    
    # Join the sorted number words into a single space-delimited string
    return ' '.join(sorted_number_words)