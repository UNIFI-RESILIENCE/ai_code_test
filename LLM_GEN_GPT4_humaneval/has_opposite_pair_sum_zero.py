def pairs_sum_to_zero(l):
    # Create a set to store the elements encountered so far
    seen = set()
    
    for num in l:
        # Check if the negative of the current number has been seen
        if -num in seen:
            return True
        # Add the current number to the set
        seen.add(num)
    
    # No such pair found
    return False