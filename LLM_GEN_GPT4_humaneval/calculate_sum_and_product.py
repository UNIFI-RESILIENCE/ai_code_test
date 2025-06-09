from typing import List, Tuple
from functools import reduce
import operator

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # Compute the sum of the numbers; for an empty list, this returns 0
    total_sum = sum(numbers)
    
    # Compute the product of the numbers; for an empty list, return 1
    total_product = reduce(operator.mul, numbers, 1)
    
    return (total_sum, total_product)