def merge_sort(arr):
    """
    Sorts the given list using the merge sort algorithm.
    
    Args:
        arr (list): The list to be sorted.
        
    Returns:
        list: The sorted list.
    """
    if len(arr) <= 1:
        return arr
    
    # Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort the halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.
    
    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.
        
    Returns:
        list: The merged and sorted list.
    """
    result = []
    left_idx = right_idx = 0
    
    # Iterate through the two lists
    while left_idx < len(left) and right_idx < len(right):
        # Add the smaller value to the result list
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # Add any remaining elements from the left list
    result.extend(left[left_idx:])
    
    # Add any remaining elements from the right list
    result.extend(right[right_idx:])
    
    return result
```

Here's how the code works:

1. The `merge_sort` function takes a list `arr` as input.
2. If the length of the list is 0 or 1, it returns the list as is (base case).
3. Otherwise, it splits the list into two halves: `left_half` and `right_half`.
4. It recursively calls `merge_sort` on the two halves, which continues to split the lists until they become single elements.
5. The `merge` function takes two sorted lists (`left` and `right`) and merges them into a single sorted list.
6. The `merge` function iterates through both lists and compares the elements at the current indices. The smaller element is added to the `result` list, and the corresponding index is incremented.
7. After one of the lists is exhausted, any remaining elements from the other list are added to the `result` list.
8. The `merge` function returns the `result` list, which is the sorted and merged list.
9. The `merge_sort` function returns the final sorted list obtained by recursively merging the sorted halves.

Here's an example usage:

```python
unsorted_list = [5, 2, 8, 1, 9, 3, 7, 4, 6]
sorted_list = merge_sort(unsorted_list)
print(sorted_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]