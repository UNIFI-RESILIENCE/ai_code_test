import math

def poly(xs: list, x: float):
    """
    Evaluates a polynomial with coefficients xs at point x.
    Polynomial form: xs[0] + xs[1]*x + xs[2]*x^2 + ... + xs[n]*x^n
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))


def find_zero(xs: list):
    """
    Finds a root (zero) of the polynomial defined by the given list of coefficients xs.
    Assumes:
        - xs has an even number of coefficients
        - The highest degree coefficient is non-zero (leading coefficient)
        These assumptions guarantee at least one real root due to the Intermediate Value Theorem.
    Uses binary search (bisection method) to find a zero numerically.
    """
    # Define a reasonable search interval
    left, right = -1e6, 1e6

    # Evaluate polynomial at the endpoints
    f_left = poly(xs, left)
    f_right = poly(xs, right)

    # Ensure the function values at the endpoints have opposite signs
    # which is a necessary condition for the bisection method
    if f_left * f_right > 0:
        raise ValueError("Function does not appear to have opposite signs at the interval bounds.")

    # Use binary search to narrow down the root
    # until the zero is found within a small tolerance
    eps = 1e-7  # acceptable error margin

    while right - left > eps:
        mid = (left + right) / 2.0
        f_mid = poly(xs, mid)

        # If the midpoint is a root or close enough, return it
        if abs(f_mid) < eps:
            return mid

        # Narrow the search interval
        if f_left * f_mid < 0:
            right = mid
            f_right = f_mid
        else:
            left = mid
            f_left = f_mid

    # Return the midpoint of the final interval as the approximate root
    return (left + right) / 2.0