To solve the find_zero function, we need to find one real root of a polynomial defined by a list of coefficients. Since the length of the list is even and the highest degree coefficient is non-zero, and we are guaranteed that a real root exists, we can use a root-finding algorithm such as the bisection method.

The bisection method requires two points where the polynomial takes opposite signs. The intermediate value theorem guarantees a root exists between such points. We repeatedly bisect the interval and update it based on the sign of the function at the midpoint.

Here's the optimized code for the prompt:

import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a real zero of the polynomial with coefficients xs.
    Assumes:
    - xs has even number of coefficients.
    - The highest-degree coefficient is non-zero.
    - A real root exists (guaranteed by the problem).
    """
    # Use bisection method
    left, right = -1e3, 1e3
    while poly(xs, left) * poly(xs, right) > 0:
        left *= 2
        right *= 2

    for _ in range(100):
        mid = (left + right) / 2
        value = poly(xs, mid)
        if abs(value) < 1e-7:
            return mid
        if poly(xs, left) * value < 0:
            right = mid
        else:
            left = mid
    return mid

This bisection method is reliable for continuous functions like polynomials when we're guaranteed the existence of a root.