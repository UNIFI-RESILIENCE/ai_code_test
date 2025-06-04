Here's the optimum implementation for the rescale_to_unit function:

from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    return [(x - min_val) / range_val for x in numbers]

Explanation:

- We compute min and max of the list.
- Subtract min from each element and divide by the range (max - min) to normalize to [0, 1] range.
- The function assumes the list has at least two distinct elements (since max != min is needed to avoid division by zero).