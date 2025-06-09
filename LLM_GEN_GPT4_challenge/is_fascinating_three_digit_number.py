def is_fascinating(n):
    # Concatenate n, 2n, and 3n into a single string
    concatenated = str(n) + str(n * 2) + str(n * 3)

    # Check if the concatenated string has exactly 9 digits
    if len(concatenated) != 9:
        return False

    # Convert the string to a set to get unique characters
    digits_set = set(concatenated)

    # Check if the set contains exactly the digits from '1' to '9'
    return digits_set == set('123456789')