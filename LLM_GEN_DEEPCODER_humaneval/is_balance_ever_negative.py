from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Check if the account balance ever falls below zero during a series of operations.
    
    Args:
        operations: A list of integers representing deposits (positive) and withdrawals (negative).
    
    Returns:
        bool: True if balance falls below zero at any point, False otherwise.
    
    Examples:
        >>> below_zero([1, 2, 3])
        False
        >>> below_zero([1, 2, -4, 5])
        True
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False