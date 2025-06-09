def min_operations_to_semi_ordered_permutation(nums):
    n = len(nums)
    index_of_one = nums.index(1)    # Find the index of 1
    index_of_n = nums.index(n)      # Find the index of n

    # If 1 is already at the start and n is already at the end, return 0
    if index_of_one == 0 and index_of_n == n - 1:
        return 0
    # If 1 is before n in the array
    elif index_of_one < index_of_n:
        # Moves required to bring 1 to the start position
        moves_for_one = index_of_one
        # Moves required to bring n to the end position
        moves_for_n = n - 1 - index_of_n
        # Total moves required
        return moves_for_one + moves_for_n
    else:
        # If 1 is after n in the array, moving 1 before n will reduce one swap
        # Moves required to bring 1 to the start position
        moves_for_one = index_of_one
        # Moves required to bring n to the end position
        moves_for_n = n - 1 - index_of_n
        # Since 1 is after n, reducing 1 swap because we can use one swap to move both
        # positions in one go during their approach (they overlap by one move)
        return moves_for_one + moves_for_n - 1

# Example usage:
print(min_operations_to_semi_ordered_permutation([2, 1, 4, 3]))  # Output: 2
print(min_operations_to_semi_ordered_permutation([2, 4, 1, 3]))  # Output: 3
print(min_operations_to_semi_ordered_permutation([1, 3, 4, 2, 5]))  # Output: 0