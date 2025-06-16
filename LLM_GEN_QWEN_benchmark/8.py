from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # Initialize sum to 0 and product to 1
    total_sum = 0
    total_product = 1
    
    # Iterate over each number in the list
    for number in numbers:
        total_sum += number       # Add the number to the total sum
        total_product *= number   # Multiply the number to the total product
    
    # Return a tuple containing the total sum and total product
    return total_sum, total_product