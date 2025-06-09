def is_fascinating(n: int) -> bool:
    # Check if the number has exactly 3 digits and is within the valid range
    if n < 100 or n > 999:
        return False
    
    # Calculate the concatenated number
    concatenated = str(n) + str(2 * n) + str(3 * n)
    
    # Check the length is exactly 9 (digits 1-9 exactly once)
    if len(concatenated) != 9:
        return False
    
    # Check for presence of '0'
    if '0' in concatenated:
        return False
    
    # Validate all digits from 1-9 are present exactly once
    unique_digits = set(concatenated)
    return len(unique_digits) == 9 and len(concatenated) == 9