import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates the polynomial with coefficients xs at point x.
    Returns the value of the polynomial: xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))


def find_zero(xs: list) -> float:
    """
    Finds x such that poly(x) = 0 for a polynomial with coefficients xs.
    Assumes xs has an even number of coefficients and the largest non-zero coefficient guarantees a solution.
    
    Uses the bisection method to find a root.
    """
    # Define a small tolerance for the root
    tolerance = 1e-7
    
    # Initial interval [-100, 100] is chosen arbitrarily. This should be adjusted based on expected root range.
    low, high = -100, 100
    
    # Ensure poly(low) and poly(high) have opposite signs
    while poly(xs, low) * poly(xs, high) > 0:
        low *= 2
        high *= 2
    
    # Bisection method
    while high - low > tolerance:
        midpoint = (low + high) / 2
        if poly(xs, midpoint) * poly(xs, low) <= 0:
            high = midpoint
        else:
            low = midpoint
    
    return (low + high) / 2


# Testing the find_zero function with the provided examples
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x, expected output: -0.5
print(round(find_zero([-6, 11, -6, 1]), 2))  # f(x) = -6 + 11x - 6x^2 + x^3, expected output: 1.0