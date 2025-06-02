def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Find the middle point to divide the array into two halves
    mid = len(arr) // 2

    # Recursively sort the first half
    left_half = merge_sort(arr[:mid])

    # Recursively sort the second half
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    # Merge the two lists while maintaining order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # If there are remaining elements in the left list, add them
    while left_index < len(left):
        sorted_list.append(left[left_index])
        left_index += 1

    # If there are remaining elements in the right list, add them
    while right_index < len(right):
        sorted_list.append(right[right_index])
        right_index += 1

    return sorted_list

# Example usage:
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original list:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted list:", sorted_arr)