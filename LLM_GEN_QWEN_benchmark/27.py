def flip_case(string: str) -> str:
    # Initialize an empty list to store the flipped characters
    flipped_chars = []
    
    # Iterate over each character in the input string
    for char in string:
        # Check if the character is lowercase
        if char.islower():
            # Convert to uppercase and append to the list
            flipped_chars.append(char.upper())
        # Check if the character is uppercase
        elif char.isupper():
            # Convert to lowercase and append to the list
            flipped_chars.append(char.lower())
        else:
            # If it's neither, append the character as is (e.g., punctuation, numbers)
            flipped_chars.append(char)
    
    # Join the list of characters into a single string and return it
    return ''.join(flipped_chars)