def modp(n: int, p: int):
    # Handle the edge case where exponent is 0
    if n == 0:
        return 1

    result = 1  # Initialize result
    base = 2 % p  # Start with base 2 modulo p

    while n > 0:
        # If n is odd, multiply the current result by the base and take modulo p
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base and reduce modulo p
        base = (base * base) % p
        # Divide n by 2 using integer division
        n //= 2

    return result