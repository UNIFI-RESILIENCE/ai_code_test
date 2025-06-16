def modp(n: int, p: int) -> int:
    # Use Python's built-in pow function with three arguments to efficiently compute (2^n) % p
    # This function uses modular exponentiation which is much more efficient than computing 2^n first and then taking modulo
    return pow(2, n, p)

# Example usage:
# print(modp(3, 5))     # Output should be 3
# print(modp(1101, 101)) # Output should be 2
# print(modp(0, 101))   # Output should be 1
# print(modp(3, 11))    # Output should be 8
# print(modp(100, 101))  # Output should be 1