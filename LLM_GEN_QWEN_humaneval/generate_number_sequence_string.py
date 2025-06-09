def string_sequence(n: int) -> str:
    # Generate a list of integers from 0 to n inclusive
    sequence = list(range(n + 1))
    
    # Convert each integer in the list to a string
    string_numbers = map(str, sequence)
    
    # Join the list of string numbers with a space delimiter to form the final output string
    return ' '.join(string_numbers)

# Metadata dictionary to store author and dataset information
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

# Function to check the correctness of the string_sequence function
def check(candidate):
    # Test case: sequence up to 0 should return '0'
    assert candidate(0) == '0'
    
    # Test case: sequence up to 3 should return '0 1 2 3'
    assert candidate(3) == '0 1 2 3'
    
    # Test case: sequence up to 10 should return '0 1 2 3 4 5 6 7 8 9 10'
    assert candidate(10) == '0 1 2 3 4 5 6 7 8 9 10'

# Run the check function to validate the string_sequence function
check(string_sequence)