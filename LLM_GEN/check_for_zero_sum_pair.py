Here is the optimum implementation for the pairs_sum_to_zero function:

def pairs_sum_to_zero(l):
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False

Explanation:

- We iterate through the list once.
- For each number, we check if its additive inverse (i.e., -num) has already been seen.
- If so, we return True, since that pair sums to zero.
- If we finish the loop without finding such a pair, we return False.

This solution is optimal because:

- Time complexity is O(n), where n is the number of elements in the list.
- Space complexity is O(n) in the worst case for storing elements in the set.

It passes all the provided test cases.