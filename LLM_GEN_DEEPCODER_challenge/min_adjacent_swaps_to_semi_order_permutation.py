def semi_ordered_permutation(nums):
    """
    Calculate the minimum number of adjacent swaps needed to make the permutation semi-ordered.
    A semi-ordered permutation has 1 at the first position and n at the last position.
    
    Args:
        nums (List[int]): A 0-indexed permutation of integers from 1 to n.
    
    Returns:
        int: The minimum number of adjacent swaps required.
    """
    n = len(nums)
    pos1 = nums.index(1)
    posn = nums.index(n)
    
    # The number of swaps to bring 1 to the first position is pos1.
    # The number of swaps to bring n to the last position is (n - 1 - posn).
    # However, if 1 is to the right of n, swapping 1 leftwards will shift n right by one.
    if pos1 > posn:
        return pos1 + (n - 1 - posn) - 1
    else:
        return pos1 + (n - 1 - posn)