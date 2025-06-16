def minimumOperations(nums):
    n = len(nums)

    # Find the current index of 1 (should be moved to the front)
    first_index = nums.index(1)

    # Find the current index of n (should be moved to the end)
    last_index = nums.index(n)

    # Total swap operations needed:
    # Move '1' to the front: requires first_index swaps
    # Move 'n' to the end: requires (n - 1 - last_index) swaps
    # If '1' comes after 'n', moving '1' left will shift 'n' right, so reduce one count
    ops = first_index + (n - 1 - last_index)
    if first_index > last_index:
        ops -= 1  # Adjust for overlap when '1' comes after 'n'

    return ops