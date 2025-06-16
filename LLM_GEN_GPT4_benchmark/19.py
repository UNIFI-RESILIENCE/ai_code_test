from typing import List

def sort_numbers(numbers: str) -> str:
    # Mapping of number words to their corresponding integer values
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

    # Mapping of integer values back to their corresponding number words
    num_to_word = {v: k for k, v in word_to_num.items()}

    # Split the input string into individual number words
    words = numbers.split()

    # Convert number words to integers for sorting
    numeric_values = [word_to_num[word] for word in words]

    # Sort the numeric values
    sorted_numeric_values = sorted(numeric_values)

    # Convert sorted integers back to their word representation
    sorted_words = [num_to_word[num] for num in sorted_numeric_values]

    # Join the sorted words back into a space-separated string
    return ' '.join(sorted_words)