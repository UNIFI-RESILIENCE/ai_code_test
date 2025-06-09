def min_cost_to_make_string_equal(s):
    n = len(s)
    # The target is either all 0s or all 1s; we need to check both possibilities.
    # We'll compute the minimal cost for both targets and return the minimum of the two.
    
    # Precompute the cost for making the string all 0s or all 1s.
    # The approach involves finding the optimal points where we switch from prefix to suffix operations.
    
    # For target 0:
    # Iterate through the string and find the positions where s[i] is '1' followed by '0's or vice versa.
    # Similarly for target 1.
    
    # The minimal cost is the minimal sum of (i+1) for some i in prefix operations and (n-j) for some j in suffix operations.
    
    # Initialize variables to compute the minimal cost for target 0 and target 1.
    cost0 = 0  # cost to make all characters 0
    cost1 = 0  # cost to make all characters 1
    
    # To make all 0s:
    # The idea is that for each '1' in the string, you might flip it either by a prefix operation ending at i or a suffix operation starting at i.
    # The optimal way is to find segments where consecutive 1s can be flipped with a single operation.
    # Similarly for target 1.
    
    # We'll compute prefix and suffix arrays to help with this.
    
    # For target 0:
    # The string should be 0...0. So whenever there's a 1 followed by a 0, it's better to flip the 1s before the 0.
    # Similarly for target 1.
    
    # Another approach: The minimal cost is the minimal sum of (i+1) for some i where s[i] is the last 1 in a block of 1s, plus (n-j) for some j where s[j] is the first 1 in a block.
    # But this needs careful handling.
    
    # Let's think differently: The operations are non-overlapping or overlapping in a way that the total cost is minimized.
    # The problem resembles covering all 1s (for target 0) or 0s (for target 1) with intervals where each interval is either a prefix or suffix, and the sum of their costs is minimized.
    
    # For target 0:
    # The 1s must be flipped. For each group of consecutive 1s, the minimal cost is min(i+1 for the last 1 in the group, n-j for the first 1 in the group).
    # But groups may require multiple operations.
    
    # For example, in "010101", the 1s are at positions 1,3,5. To flip them:
    # Option 1: Use prefix operations for each 1: cost 2 + 4 +6 = 12.
    # Option 2: Use suffix operations for each 1: cost 5 +3 +1 =9 (as in the example).
    # So the minimal cost is 9.
    
    # So for target 0, the minimal cost is the sum of the minimal costs to flip each group of 1s (either by prefix or suffix).
    # Similarly for target 1.
    
    # So the approach is:
    # For target 0:
    #   Split the string into groups of 0s and 1s.
    #   For each group of 1s, the cost to flip them is min( (last index in group +1), (n - first index in group) ).
    #   Sum these minimal costs for all 1 groups.
    # Similarly for target 1.
    
    # Then the answer is the min of the two totals.
    
    # Let's implement this.
    
    groups0 = []  # groups of 1s for target 0
    groups1 = []  # groups of 0s for target 1
    
    # Process the string to find groups of consecutive 1s (for target 0) and 0s (for target 1)
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '1':
            start = i
            while i < n and s[i] == '1':
                i += 1
            groups0.append((start, i-1))
        else:
            i += 1
    
    i = 0
    while i < n:
        if s[i] == '0':
            start = i
            while i < n and s[i] == '0':
                i += 1
            groups1.append((start, i-1))
        else:
            i += 1
    
    # Calculate cost for target 0 (all 0s)
    total_cost0 = 0
    for start, end in groups0:
        cost_prefix = end + 1
        cost_suffix = n - start
        total_cost0 += min(cost_prefix, cost_suffix)
    
    # Calculate cost for target 1 (all 1s)
    total_cost1 = 0
    for start, end in groups1:
        cost_prefix = end + 1
        cost_suffix = n - start
        total_cost1 += min(cost_prefix, cost_suffix)
    
    return min(total_cost0, total_cost1)