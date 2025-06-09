import string
from random import randint, choice


# Function to encode a string by shifting each character by 5 positions in the alphabet
def encode_shift(s: str) -> str:
    return "".join(chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s)


# Function to decode a string that was encoded with the `encode_shift` function
def decode_shift(s: str) -> str:
    # Shift each character back by 5 positions in the alphabet
    return "".join(chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s)


# Metadata dictionary (currently empty, can be used for additional information or configurations)
METADATA = {}


# Function to check the correctness of the `decode_shift` function using random test cases
def check(candidate):
    letters = string.ascii_lowercase
    for _ in range(100):  # Generate 100 random test cases
        # Create a random string of lowercase letters with length between 10 and 20
        original_str = ''.join(choice(letters) for _ in range(randint(10, 20)))
        # Encode the string using the `encode_shift` function
        encoded_str = encode_shift(original_str)
        # Decode the encoded string and assert that it matches the original string
        assert candidate(encoded_str) == original_str


# Example usage of the check function to verify the `decode_shift` implementation
check(decode_shift)