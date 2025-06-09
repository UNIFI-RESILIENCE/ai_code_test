import math

def poly(xs: list, x: float):
    """
    Evaluates a polynomial with coefficients `xs` at point `x`.
    Computes: xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    """
    Finds a root (zero) of the polynomial defined by the coefficient list `xs`.
    Assumes:
        - The list `xs` has an even number of coefficients.
        - The highest-degree coefficient is non-zero, ensuring at least one real root exists.
    Uses the bisection method to locate a zero of the polynomial within a defined interval.
    Returns:
        A floating-point value x such that poly(xs, x) ≈ 0
    """

    def f(x):
        # Polynomial evaluation helper using current coefficients
        return poly(xs, x)

    # Initial search interval; uses large bounds based on typical polynomial root ranges
    left, right = -1000.0, 1000.0

    # Expand interval until f(left) and f(right) have opposite signs (indicating a root in between)
    while f(left) * f(right) > 0:
        left /= 2
        right *= 2
        if abs(left) > 1e10 or abs(right) > 1e10:
            # Interval expansion failed to bracket a root (should not happen given constraints)
            raise RuntimeError("Failed to find interval bracketing the root.")

    # Bisection method loop
    for _ in range(100):
        mid = (left + right) / 2
        val = f(mid)

        # If the polynomial is approximately zero at mid, return mid
        if abs(val) < 1e-7:
            return mid

        # Determine subinterval containing sign change
        if f(left) * val < 0:
            right = mid
        else:
            left = mid

    # Return the best approximation after max iterations
    return (left + right) / 2


METADATA = {}