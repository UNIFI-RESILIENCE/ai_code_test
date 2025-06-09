from typing import List

def sort_numbers(numbers: str) -> str:
    # Mapping of word representations to their numerical values
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
    
    # Split the input string into individual number words
    number_words = numbers.split()
    
    # Sort the words based on their numerical values
    sorted_words = sorted(number_words, key=lambda word: word_to_num[word])
    
    # Join the sorted words back into a space-delimited string
    return ' '.join(sorted_words)