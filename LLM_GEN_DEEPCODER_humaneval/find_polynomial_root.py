import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero point of the polynomial with coefficients xs using the Newton-Raphson method.
    The polynomial must have an even number of coefficients and a non-zero leading coefficient.
    
    Args:
        xs: List of polynomial coefficients, where xs[0] is the constant term.
    
    Returns:
        A zero point x such that poly(xs, x) is approximately zero.
    
    Examples:
        >>> round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x
        -0.5
        >>> round(find_zero([-6, 11, -6, 1]), 2)  # (x - 1)*(x - 2)*(x - 3)
        1.0
    """
    # Derivative of the polynomial function
    def derivative(xs, x):
        return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])
    
    # Initial guess (can be adjusted; Newton-Raphson is somewhat robust to initial guess)
    x = 0.0
    
    # Newton-Raphson iteration
    for _ in range(100):  # Limit iterations to prevent infinite loops
        fx = poly(xs, x)
        if abs(fx) < 1e-6:  # Tolerance threshold
            break
        dfx = derivative(xs, x)
        if dfx == 0:  # Avoid division by zero
            x += 0.1  # Perturb x slightly
            continue
        x -= fx / dfx
    
    return x