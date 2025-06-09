def count_seniors(details):
    """
    Counts the number of passengers who are strictly more than 60 years old.
    
    Args:
    - details: A list of strings where each string contains passenger details as per the specified format.
    
    Returns:
    - int: The count of passengers with age > 60.
    """
    count = 0
    for passenger in details:
        # Extract the age part of the string (indices 11 and 12)
        age = int(passenger[11:13])
        if age > 60:
            count += 1
    return count