def triangle_area(a, h):
    # Calculate the area of a triangle using the formula: (base * height) / 2
    return 0.5 * a * h


METADATA = {}


def check(candidate):
    # Test case 1: base = 5, height = 3, expected area = 7.5
    assert candidate(5, 3) == 7.5
    # Test case 2: base = 2, height = 2, expected area = 2.0
    assert candidate(2, 2) == 2.0
    # Test case 3: base = 10, height = 8, expected area = 40.0
    assert candidate(10, 8) == 40.0