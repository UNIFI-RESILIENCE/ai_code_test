def how_many_times(string: str, substring: str) -> int:
    count = 0
    start = 0

    # Loop through the string to find all occurrences of the substring
    while True:
        # Find the next occurrence of the substring starting from the current position
        start = string.find(substring, start)
        
        # If no more occurrences are found, break the loop
        if start == -1:
            break
        
        # Increment the count for each found occurrence
        count += 1
        
        # Move the start index forward by one to allow overlapping matches
        start += 1

    return count


# Metadata about the code
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

# Function to check the correctness of the how_many_times function
def check(candidate):
    assert candidate('', 'x') == 0, "Test case 1 failed"
    assert candidate('xyxyxyx', 'x') == 4, "Test case 2 failed"
    assert candidate('cacacacac', 'cac') == 4, "Test case 3 failed"
    assert candidate('john doe', 'john') == 1, "Test case 4 failed"

# Run the check function to validate the implementation
check(how_many_times)