import string
from random import randint, choice


def encode_cyclic(s: str):
    """
    Encodes the string by cycling groups of three characters.
    """
    # Split the string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group if the group has exactly three characters
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    # Split the encoded string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Reverse the cycling process for each group of three characters
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


METADATA = {}


def check(candidate):
    letters = string.ascii_lowercase
    for _ in range(100):
        # Generate a random string of length between 10 and 20
        original_str = ''.join(choice(letters) for i in range(randint(10, 20)))
        # Encode the random string
        encoded_str = encode_cyclic(original_str)
        # Decode the encoded string and assert it matches the original string
        assert candidate(encoded_str) == original_str


# Example usage:
if __name__ == "__main__":
    example_str = "abcdefg"
    encoded = encode_cyclic(example_str)
    print(f"Encoded: {encoded}")
    decoded = decode_cyclic(encoded)
    print(f"Decoded: {decoded}")

    # Run the check function to validate the decode_cyclic implementation
    check(decode_cyclic)