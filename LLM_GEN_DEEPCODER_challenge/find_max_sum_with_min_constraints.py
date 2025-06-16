import bisect

def maximumSumQueries(nums1, nums2, queries):
    n = len(nums1)
    # Create a list of tuples (a, b, a + b) for each element in nums1 and nums2
    elements = []
    for a, b in zip(nums1, nums2):
        elements.append((a, b, a + b))
    
    # Sort the elements in descending order of a (nums1), then descending b (nums2)
    elements.sort(reverse=True, key=lambda x: (x[0], x[1]))
    
    # Extract the b values (nums2) and prepare a sorted list of unique b values for coordinate compression
    b_values = [b for a, b, s in elements]
    unique_b = sorted(set(b_values))
    # Create a mapping from b value to its compressed index
    b_to_idx = {v: i for i, v in enumerate(unique_b)}
    
    # Build a segment tree to handle range maximum queries on the compressed b indices
    class SegmentTree:
        def __init__(self, size):
            self.n = 1
            while self.n < size:
                self.n <<= 1
            self.tree = [-1] * (2 * self.n)
        
        def update(self, idx, val):
            idx += self.n
            if self.tree[idx] < val:
                self.tree[idx] = val
                while idx > 1:
                    idx >>= 1
                    new_val = max(self.tree[2*idx], self.tree[2*idx +1])
                    if self.tree[idx] == new_val:
                        break
                    self.tree[idx] = new_val
        
        def query(self, l, r):
            res = -1
            l += self.n
            r += self.n
            while l <= r:
                if l % 2 == 1:
                    res = max(res, self.tree[l])
                    l += 1
                if r % 2 == 0:
                    res = max(res, self.tree[r])
                    r -= 1
                l >>= 1
                r >>= 1
            return res
    
    st = SegmentTree(len(unique_b))
    res = []
    ptr = 0
    # Process queries in an order that allows us to use the segment tree efficiently
    # We need to sort the queries in descending order of x_i, and process them in that order
    # Along with the elements sorted in descending a (nums1)
    # So, we can process elements in order and answer queries in order
    
    # Prepare the queries with their original indices to sort them and then reconstruct the answer
    sorted_queries = []
    for i in range(len(queries)):
        x, y = queries[i]
        sorted_queries.append((x, y, i))
    # Sort queries in descending order of x
    sorted_queries.sort(reverse=True, key=lambda q: q[0])
    
    answer = [0] * len(queries)
    for x, y, original_idx in sorted_queries:
        # Process all elements with a >= x that haven't been processed yet
        while ptr < n and elements[ptr][0] >= x:
            a, b, s = elements[ptr]
            # Compress the b coordinate
            compressed_b = b_to_idx[b]
            # Update the segment tree at this compressed_b with the sum s
            st.update(compressed_b, s)
            ptr += 1
        
        # Now, query the segment tree for b >= y
        # Find the smallest index in unique_b >= y
        left = bisect.bisect_left(unique_b, y)
        if left >= len(unique_b):
            # No such b exists
            answer[original_idx] = -1
        else:
            max_sum = st.query(left, len(unique_b) - 1)
            answer[original_idx] = max_sum if max_sum != -1 else -1
    return answer