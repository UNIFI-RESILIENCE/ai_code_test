def does_valid_original_exist(derived):
    # Initialize a variable to hold the XOR of all derived elements
    xor_sum = 0

    # Iterate through the derived array and compute the XOR sum
    for val in derived:
        xor_sum ^= val  # XOR accumulates over each value

    # If the XOR sum of all elements in derived is 0, a valid original exists
    return xor_sum == 0
