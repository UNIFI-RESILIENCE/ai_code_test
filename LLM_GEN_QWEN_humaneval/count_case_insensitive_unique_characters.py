def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ensure case insensitivity
    lower_string = string.lower()
    
    # Use a set to store distinct characters since sets inherently do not allow duplicates
    distinct_chars = set(lower_string)
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Metadata about the code author and dataset
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    # Test cases to validate the solution
    assert candidate('') == 0, "Empty string should have 0 distinct characters"
    assert candidate('abcde') == 5, "String with all unique characters"
    assert candidate('abcde' + 'cade' + 'CADE') == 5, "String with repeated characters, different cases"
    assert candidate('aaaaAAAAaaaa') == 1, "String with only one unique character"
    assert candidate('Jerry jERRY JeRRRY') == 5, "String with mixed case and repeated characters"


# Run the check function with the count_distinct_characters function as an argument
check(count_distinct_characters)