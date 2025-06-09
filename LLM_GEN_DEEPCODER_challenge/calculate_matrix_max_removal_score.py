def matrix_score(nums):
    score = 0
    # Process each column (step) until all rows are empty
    while any(nums):
        max_numbers = []
        for row in nums:
            if row:
                # Find and remove the largest element in the row
                max_num = max(row)
                row.remove(max_num)
                max_numbers.append(max_num)
        if max_numbers:
            # Add the highest number from this step to the score
            score += max(max_numbers)
    return score