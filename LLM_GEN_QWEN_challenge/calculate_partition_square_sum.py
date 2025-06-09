def can_partition(num_str, target):
    """
    Helper function to check if the given string can be partitioned into sums equal to the target.

    :param num_str: String representation of the number to partition.
    :param target: Integer value which the partitions should sum up to.
    :return: Boolean indicating whether the partitioning is possible.
    """
    # Base case: if the entire string represents the target, return True
    if int(num_str) == target:
        return True
    
    len_str = len(num_str)
    
    # Recursive case: try partitioning the string at every position
    for i in range(1, len_str):
        # Convert the partition to an integer
        current_part = int(num_str[:i])
        
        # Early termination if current part exceeds the target
        if current_part > target:
            break
        
        # Recursively check if the remaining string can sum to the remaining target
        remaining_target = target - current_part
        if can_partition(num_str[i:], remaining_target):
            return True
    
    # If no valid partitioning was found, return False
    return False


def punishment_number(n):
    """
    Calculate the punishment number of n.

    :param n: Positive integer.
    :return: Sum of squares of all integers i from 1 to n that meet the criteria.
    """
    total_punishment = 0
    
    # Iterate over each integer from 1 to n
    for i in range(1, n + 1):
        squared = str(i * i)
        
        # Check if the square of the integer can be partitioned to sum to the integer itself
        if can_partition(squared, i):
            total_punishment += i * i
    
    return total_punishment


# Example usage:
# n = 10 should return 182
result_1 = punishment_number(10)
print(f"Punishment number for n=10 is {result_1}")

# n = 37 should return 1478
result_2 = punishment_number(37)
print(f"Punishment number for n=37 is {result_2}")