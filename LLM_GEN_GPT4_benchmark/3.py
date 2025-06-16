from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0  # Initialize account balance to zero

    for op in operations:
        balance += op  # Apply deposit or withdrawal operation
        if balance < 0:
            return True  # Balance has fallen below zero
    
    return False  # Balance never went below zero after all operations