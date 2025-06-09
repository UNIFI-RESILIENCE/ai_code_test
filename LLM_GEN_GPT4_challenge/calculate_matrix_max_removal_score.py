from typing import List

def matrixScore(nums: List[List[int]]) -> int:
    # Sort each row in ascending order to make it easy to remove max values later
    for row in nums:
        row.sort()
    
    score = 0
    num_cols = len(nums[0])
    
    # Iterate over columns right to left (since rows were sorted ascending)
    for col in range(num_cols - 1, -1, -1):
        max_val = 0
        # For each row, get the current largest (rightmost) remaining value
        for row in nums:
            max_val = max(max_val, row[col])
        # Add the highest value among removed maximums to the score
        score += max_val
    
    return score