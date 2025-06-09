def isValidDerived(derived):
    # Helper function to check if 'original' can form the given 'derived'
    def check(original_start):
        original = [original_start]
        for i in range(1, len(derived)):
            next_value = derived[i-1] ^ original[-1]
            original.append(next_value)
        # Finally, check the circular condition
        return derived[-1] == (original[-1] ^ original[0])
    
    # Try both starting possibilities for the first element of 'original'
    if check(0) or check(1):
        return True
    else:
        return False

# Example usage:
print(isValidDerived([1, 1, 0]))  # Output: True
print(isValidDerived([1, 1]))     # Output: True
print(isValidDerived([1, 0]))     # Output: False