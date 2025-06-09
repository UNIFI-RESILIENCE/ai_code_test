from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """Returns a tuple containing the sum and product of all integers in the input list.
    
    Args:
        numbers: A list of integers to compute the sum and product for.
        
    Returns:
        A tuple (sum, product) where:
            - sum is the sum of all integers in the list (0 for an empty list).
            - product is the product of all integers in the list (1 for an empty list).
            
    Examples:
        >>> sum_product([])
        (0, 1)
        >>> sum_product([1, 2, 3, 4])
        (10, 24)
    """
    # Compute the sum of the numbers (default to 0 for empty list)
    total_sum = sum(numbers)
    
    # Compute the product of the numbers (default to 1 for empty list)
    product = 1
    for num in numbers:
        product *= num
    
    return (total_sum, product)