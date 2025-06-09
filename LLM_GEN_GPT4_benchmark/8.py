from typing import List, Tuple
from functools import reduce
import operator

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # Calculate the sum of the list; returns 0 if the list is empty
    total_sum = sum(numbers)

    # Calculate the product of the list; returns 1 if the list is empty
    total_product = reduce(operator.mul, numbers, 1)

    return total_sum, total_product