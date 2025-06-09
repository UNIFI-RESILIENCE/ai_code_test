from bisect import bisect_left
from collections import defaultdict

def maximum_sum_with_constraints(nums1, nums2, queries):
    # Zip nums1 and nums2 to form points and compute sum values
    points = list(zip(nums1, nums2))
    pairs = sorted(((a, b, a + b) for (a, b) in points), reverse=True)

    # Sort queries and keep original indices to return results in original order
    indexed_queries = sorted([(x, y, idx) for idx, (x, y) in enumerate(queries)], reverse=True)

    # Compress y-coordinates to optimize segment tree size
    all_y = sorted(set(b for _, b in points).union(y for _, y, _ in indexed_queries))
    y_to_idx = {val: idx for idx, val in enumerate(all_y)}

    # Segment tree implementation for range max query and point update
    class SegmentTree:
        def __init__(self, size):
            self.N = 1
            while self.N < size:
                self.N <<= 1
            self.tree = [-1] * (2 * self.N)

        def update(self, idx, value):
            idx += self.N
            self.tree[idx] = max(self.tree[idx], value)
            while idx > 1:
                idx >>= 1
                self.tree[idx] = max(self.tree[2 * idx], self.tree[2 * idx + 1])

        def query(self, left, right):
            res = -1
            left += self.N
            right += self.N
            while left < right:
                if left % 2:
                    res = max(res, self.tree[left])
                    left += 1
                if right % 2:
                    right -= 1
                    res = max(res, self.tree[right])
                left >>= 1
                right >>= 1
            return res

    st = SegmentTree(len(all_y))

    ans = [0] * len(queries)
    i = 0  # pointer to iterate through pairs

    for x, y, qidx in indexed_queries:
        # Process all points where nums1 >= x
        while i < len(pairs) and pairs[i][0] >= x:
            _, b, total = pairs[i]
            st.update(y_to_idx[b], total)
            i += 1

        # Query segment tree for max sum where nums2 >= y
        idx_y = bisect_left(all_y, y)
        if idx_y < len(all_y):
            ans[qidx] = st.query(idx_y, len(all_y))
        else:
            ans[qidx] = -1  # No valid nums2[j] >= y

    return ans