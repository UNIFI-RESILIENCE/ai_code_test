from typing import List

def string_xor(a: str, b: str) -> str:
    # Ensure both input strings are of the same length
    if len(a) != len(b):
        raise ValueError("Input strings must be of the same length.")

    # Initialize an empty list to store XOR results
    xor_result = []

    # Iterate over each pair of characters from both strings
    for char_a, char_b in zip(a, b):
        # Perform XOR operation for the current pair of characters
        # Convert characters to integers, perform XOR, and convert back to string
        xor_result.append(str(int(char_a) ^ int(char_b)))

    # Join the list of XOR results into a single string and return
    return ''.join(xor_result)