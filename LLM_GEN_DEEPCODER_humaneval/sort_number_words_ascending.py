from typing import List

def sort_numbers(numbers: str) -> str:
    """Sorts a space-delimited string of number words from 'zero' to 'nine' in ascending numerical order.
    
    Args:
        numbers: A string containing space-separated number words (e.g., 'three one five').
    
    Returns:
        A string with the number words sorted in ascending numerical order (e.g., 'one three five').
    
    Raises:
        ValueError: If any word in the input string is not a valid number word from 'zero' to 'nine'.
    """
    if not numbers.strip():
        return numbers
    
    # Mapping of number words to their corresponding numerical values
    word_to_num = {
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
    
    # Split the input string into individual words
    number_words = numbers.split()
    
    # Sort the words based on their numerical values
    sorted_words = sorted(number_words, key=lambda word: word_to_num[word])
    
    # Join the sorted words back into a space-delimited string
    return ' '.join(sorted_words)