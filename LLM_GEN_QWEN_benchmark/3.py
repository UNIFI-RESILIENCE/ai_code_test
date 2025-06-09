from typing import List

def below_zero(operations: List[int]) -> bool:
    # Initialize the starting balance to zero
    balance = 0
    
    # Iterate through each operation in the list
    for operation in operations:
        # Update the balance by adding the current operation (deposit or withdrawal)
        balance += operation
        
        # Check if the balance has fallen below zero
        if balance < 0:
            # If it has, immediately return True indicating that
            # the balance was below zero at some point
            return True
    
    # If the loop completes without the balance falling below zero,
    # return False indicating that the balance never went below zero
    return False