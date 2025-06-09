def minimum_operations(num1: int, num2: int) -> int:
    # The possible values we can subtract from num1 are:
    # val = 2^i + num2, for i in range(0, 61)
    # Let's precompute all possible values we can subtract
    subtract_vals = [ (1 << i) + num2 for i in range(61) ]

    # To reach 0 from num1, we can reverse the thinking:
    # Try to construct num1 as a sum of some subset of subtract_vals.
    # The optimal way is to use operations greedily by 2^i order.

    # Since the space of subtract_vals is not too large (61 values), 
    # we'll perform a greedy search trying all combinations of using these
    # values, but we need to make sure all values used are positive.
    operations = 0
    target = num1

    # Sort the valid values in decreasing order to use large effects first
    valid_subtracts = [val for val in subtract_vals if val > 0]
    valid_subtracts.sort(reverse=True)

    for val in valid_subtracts:
        if target <= 0:
            break
        # Count how many times val fits in target
        count = target // val
        operations += count
        target -= count * val

    # After greedy subtracting, if target is 0, we succeeded
    if target == 0:
        return operations
    else:
        return -1