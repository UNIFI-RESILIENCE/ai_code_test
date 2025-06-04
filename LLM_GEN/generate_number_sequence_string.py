Here's the optimum implementation for the given problem:

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 up to n inclusive. """
    return ' '.join(str(i) for i in range(n + 1))

This implementation uses a generator expression with join for efficient string construction.