Here's the optimal implementation for the sum_product function:

from typing import List, Tuple
from functools import reduce
import operator

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    return (sum(numbers), reduce(operator.mul, numbers, 1))

This version uses built-in Python functions to efficiently compute the sum and product. functools.reduce with operator.mul is used for the product, which returns 1 for empty lists (the correct identity for multiplication).