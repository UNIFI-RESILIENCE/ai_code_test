def remove_trailing_zeros(num):
    # Initialize a variable to track the position of the last non-zero character
    last_non_zero_index = len(num) - 1

    # Find the index of the last non-zero digit
    while last_non_zero_index >= 0:
        if num[last_non_zero_index] != '0':
            break
        last_non_zero_index -= 1

    # Return the substring from the start to the last non-zero digit index + 1
    return num[:last_non_zero_index + 1]

# Example usage:
# Input: num = "51230100"
# Output: "512301"
print(remove_trailing_zeros("51230100"))

# Input: num = "123"
# Output: "123"
print(remove_trailing_zeros("123"))