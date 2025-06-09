import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    """
    Finds a zero point for the polynomial with coefficients xs using the bisection method.
    Assumes:
    - xs has even length (guarantees at least one real root for odd-degree polynomials)
    - The highest degree coefficient is non-zero
    
    Args:
        xs: List of polynomial coefficients, starting from x^0 to x^n
        
    Returns:
        float: A root of the polynomial within a reasonable range
        
    Examples:
        >>> round(find_zero([1, 2]), 2)
        -0.5
        >>> round(find_zero([-6, 11, -6, 1]), 2)
        1.0
    """
    # Determine the degree of the polynomial (highest power with non-zero coefficient)
    degree = len(xs) - 1
    while degree > 0 and math.isclose(xs[degree], 0, abs_tol=1e-9):
        degree -= 1
    
    # Initial bounds for bisection (can be adjusted based on polynomial behavior)
    left, right = -1.0, 1.0
    
    # Expand search window until we bracket a root
    # (since odd-degree polynomials tend to -inf and +inf at extremes)
    while poly(xs, left) * poly(xs, right) > 0:
        left *= 2
        right *= 2
    
    # Bisection method to find root
    tolerance = 1e-9
    max_iterations = 1000
    for _ in range(max_iterations):
        mid = (left + right) / 2
        val = poly(xs, mid)
        
        if abs(val) < tolerance:
            return mid
        
        if val * poly(xs, left) < 0:
            right = mid
        else:
            left = mid
    
    return (left + right) / 2  # Return best estimate if tolerance not met