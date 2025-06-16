def unique(l: list):
    # Convert list to a set to remove duplicates
    # Then convert back to a list and sort the elements
    return sorted(set(l))


METADATA = {}


def check(candidate):
    # Test with a list containing duplicates
    assert candidate([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]