def maxScore(nums):
    # Initialize the score to zero
    score = 0
    
    # Continue the process until the matrix is empty
    while nums:
        # Extract the largest element from each row and store them in a list
        max_elements = []
        for row in nums:
            # Sort the row in descending order to easily access the largest element
            row.sort(reverse=True)
            # Append the largest element (first element after sorting) to max_elements
            max_elements.append(row[0])
        
        # Add the maximum of the extracted largest elements to the score
        score += max(max_elements)
        
        # Remove the selected largest elements from their respective rows
        for row in nums:
            row.pop(0)  # Remove the first element since it's already used
        
        # Remove any empty rows that have been fully processed
        nums = [row for row in nums if row]
    
    # Return the final computed score
    return score


# Example usage:
nums1 = [[7, 2, 1], [6, 4, 2], [6, 5, 3], [3, 2, 1]]
nums2 = [[1]]

print(maxScore(nums1))  # Output: 15
print(maxScore(nums2))  # Output: 1