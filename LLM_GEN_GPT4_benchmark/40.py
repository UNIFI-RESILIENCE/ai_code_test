from itertools import combinations

def triples_sum_to_zero(l: list) -> bool:
    # Early return if list has fewer than 3 elements
    if len(l) < 3:
        return False

    # Use set to avoid checking duplicate tuples if input contains duplicates
    seen = set()

    # Iterate over all possible unique triplets in the list
    for a, b, c in combinations(l, 3):
        # Sort the triple to avoid permutations of the same values
        triplet = tuple(sorted((a, b, c)))
        if triplet in seen:
            continue
        seen.add(triplet)

        # Check if the triplet sums to zero
        if a + b + c == 0:
            return True

    # No matching triplet found
    return False