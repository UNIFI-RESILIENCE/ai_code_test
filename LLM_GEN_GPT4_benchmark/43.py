def pairs_sum_to_zero(l):
    # Create a set to store the numbers we've seen so far
    seen = set()

    # Iterate through each number in the list
    for num in l:
        # Check if the negative of the current number exists in the set
        if -num in seen:
            return True
        # Add the current number to the set
        seen.add(num)

    # If no such pair is found, return False
    return False