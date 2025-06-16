from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Computes the sum and product of all integers in the input list.
    
    Args:
        numbers: List of integers to compute sum and product for.
        
    Returns:
        Tuple containing (sum, product) of the numbers. For empty list, returns (0, 1).
    """
    total_sum = 0
    product = 1
    
    for num in numbers:
        total_sum += num
        product *= num
        
    return (total_sum, product)