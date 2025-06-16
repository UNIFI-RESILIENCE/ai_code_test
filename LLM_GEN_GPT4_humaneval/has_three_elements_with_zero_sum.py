def triples_sum_to_zero(l: list) -> bool:
    # Sort the list to utilize two-pointer technique efficiently
    l.sort()
    n = len(l)

    # Loop through each element, using it as the first element of the triplet
    for i in range(n - 2):
        # Skip duplicate elements to avoid checking the same triplet
        if i > 0 and l[i] == l[i - 1]:
            continue

        # Two pointers initialization
        left = i + 1
        right = n - 1

        # Check combinations using two-pointer approach
        while left < right:
            current_sum = l[i] + l[left] + l[right]
            if current_sum == 0:
                return True  # Found a valid triplet
            elif current_sum < 0:
                left += 1  # Need a larger number
            else:
                right -= 1  # Need a smaller number

    # No valid triplet found
    return False