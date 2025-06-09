from typing import List

def sort_numbers(numbers: str) -> str:
    # Mapping from number words to their numeric values
    num_word_to_int = {
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

    # Mapping from numeric values back to number words
    int_to_num_word = {value: key for key, value in num_word_to_int.items()}

    if not numbers:
        return ''

    # Split the input string into individual number words
    words = numbers.split()

    # Convert number words to integers for sorting
    nums = sorted(num_word_to_int[word] for word in words)

    # Convert sorted numbers back to words
    sorted_words = [int_to_num_word[num] for num in nums]

    # Join the sorted words back into a space-delimited string
    return ' '.join(sorted_words)