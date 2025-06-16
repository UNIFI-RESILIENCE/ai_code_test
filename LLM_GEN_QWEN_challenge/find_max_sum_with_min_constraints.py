from sortedcontainers import SortedList

def process_queries(nums1, nums2, queries):
    # Step 1: Pair and sort the arrays by nums1 in descending order
    pairs = sorted(zip(nums1, nums2), reverse=True)
    
    # Step 2: Prepare to sort queries by x_i in descending order
    # Also keep track of the original index for answering
    indexed_queries = [(x, y, i) for i, (x, y) in enumerate(queries)]
    indexed_queries.sort(reverse=True)
    
    # Step 3: Initialize the sorted list for nums2 and max sums
    sl = SortedList()
    
    # Step 4: Initialize the answer list
    answer = [-1] * len(queries)
    
    # Step 5: Process each query
    query_index = 0
    pair_index = 0
    
    while query_index < len(queries) and pair_index < len(pairs):
        x, y, original_index = indexed_queries[query_index]
        
        # Step 6: Add pairs to the sorted list until nums1 is less than x
        while pair_index < len(pairs) and pairs[pair_index][0] >= x:
            nums1_val, nums2_val = pairs[pair_index]
            sl.add((nums2_val, nums1_val + nums2_val))
            pair_index += 1
        
        # Step 7: Binary search for the maximum sum with nums2 >= y
        idx = sl.bisect_left((y, float('-inf')))
        
        if idx < len(sl):
            answer[original_index] = sl[idx][1]
        
        # Step 8: Move to the next query
        query_index += 1
    
    return answer

# Example usage
nums1 = [4, 3, 1, 2]
nums2 = [2, 4, 9, 5]
queries = [[4, 1], [1, 3], [2, 5]]
print(process_queries(nums1, nums2, queries))  # Output: [6, 10, 7]

nums1 = [3, 2, 5]
nums2 = [2, 3, 4]
queries = [[4, 4], [3, 2], [1, 1]]
print(process_queries(nums1, nums2, queries))  # Output: [9, 9, 9]

nums1 = [2, 1]
nums2 = [2, 3]
queries = [[3, 3]]
print(process_queries(nums1, nums2, queries))  # Output: [-1]