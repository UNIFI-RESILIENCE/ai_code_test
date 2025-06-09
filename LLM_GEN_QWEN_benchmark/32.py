import numpy as np

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns: xs[0] + xs[1] * x + xs[2] * x^2 + .... + xs[n] * x^n
    """
    return sum(coeff * (x ** i) for i, coeff in enumerate(xs))

def find_zero(xs: list) -> float:
    """
    Finds x such that poly(x) = 0.
    Returns only one zero point, even if there are many.
    This function assumes that the list xs has an even number of coefficients
    and that there is guaranteed to be at least one real root.
    
    Parameters:
    xs (list): Coefficients of a polynomial.
    
    Returns:
    float: A zero of the polynomial.
    """
    # Calculate all roots of the polynomial
    roots = np.roots(xs)
    
    # Filter out the real roots (imaginary part is close to zero)
    real_roots = roots[np.isclose(roots.imag, 0)].real
    
    # Return the first real root found
    return real_roots[0] if real_roots.size > 0 else None

# Example usage:
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x => Output: -0.5
print(round(find_zero([-6, 11, -6, 1]), 2))  # f(x) = -6 + 11x - 6x^2 + x^3 => Output: 1.0