def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to make the comparison case-insensitive
    normalized_string = string.lower()
    
    # Use a set to store unique characters
    distinct_characters = set(normalized_string)
    
    # Return the number of unique characters
    return len(distinct_characters)