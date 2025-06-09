def count_distinct_characters(string: str) -> int:
    # Convert the input string to lowercase to ensure case-insensitive comparison
    normalized_string = string.lower()
    
    # Use a set to store unique characters
    unique_characters = set()

    # Iterate over each character in the normalized string
    for char in normalized_string:
        # Consider only non-space characters for uniqueness
        if char != ' ':
            unique_characters.add(char)

    # Return the number of unique characters
    return len(unique_characters)


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    # Edge case: empty string should return 0
    assert candidate('') == 0

    # Basic distinct characters test
    assert candidate('abcde') == 5

    # Repeating characters with different cases should count as one
    assert candidate('abcde' + 'cade' + 'CADE') == 5

    # Only one unique character despite repetition and casing
    assert candidate('aaaaAAAAaaaa') == 1

    # Characters and spaces included; should count distinct non-space characters case-insensitively
    assert candidate('Jerry jERRY JeRRRY') == 5