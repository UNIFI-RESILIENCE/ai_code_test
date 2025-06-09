def pairs_sum_to_zero(l):
    # Create a set to store the elements we have seen so far
    seen = set()
    
    # Iterate over each element in the list
    for number in l:
        # Calculate the opposite number that would sum to zero with the current number
        opposite = -number
        
        # Check if the opposite number is already in the set
        if opposite in seen:
            # If it is, we found a pair that sums to zero
            return True
        
        # Add the current number to the set
        seen.add(number)
    
    # If no pairs were found, return False
    return False