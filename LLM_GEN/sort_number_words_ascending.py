Here is the optimum implementation for the sort_numbers function:

from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    if not numbers:
        return ''
    
    # Mapping words to their respective numeric values
    word_to_number = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    number_to_word = {v: k for k, v in word_to_number.items()}

    # Split, convert to digits, sort, convert back to words
    words = numbers.split()
    sorted_words = sorted(words, key=lambda word: word_to_number[word])
    return ' '.join(sorted_words)

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):
    assert candidate('') == ''
    assert candidate('three') == 'three'
    assert candidate('three five nine') == 'three five nine'
    assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
    assert candidate('six five four three two one zero') == 'zero one two three four five six'

This implementation:
- Handles empty input.
- Uses a dictionary to map number words to numeric values for sorting.
- Sorts the input words based on their numeric values.
- Returns the result as a space-separated sorted string.