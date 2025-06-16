def count_distinct_characters(string: str) -> int:
    # Convert the string to lower case to ensure case insensitivity
    lower_case_string = string.lower()
    
    # Use a set to store distinct characters, as sets automatically handle uniqueness
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)

# Example usage:
# print(count_distinct_characters('xyzXYZ'))  # Output: 3
# print(count_distinct_characters('Jerry'))   # Output: 4