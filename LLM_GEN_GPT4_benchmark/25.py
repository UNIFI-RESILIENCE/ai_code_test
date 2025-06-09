from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    # Start dividing from the smallest prime number
    divisor = 2
    while divisor * divisor <= n:
        # While n is divisible by current divisor, append it and divide n
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    # If remaining n is greater than 1, it is a prime number
    if n > 1:
        factors.append(n)
    return factors