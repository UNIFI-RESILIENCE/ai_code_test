Here's the optimum implementation of the change_base function described in your prompt:

def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    base numbers are less than 10.
    """
    if x == 0:
        return "0"
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    return ''.join(reversed(digits))

This implementation uses a simple loop to repeatedly divide the input number x by the target base and collects the remainders, which correspond to the digits of the number in the new base. After collecting the digits in reverse order (from least significant to most significant), it reverses them to return the final string representation. This satisfies all conditions in the problem specification and the provided tests.