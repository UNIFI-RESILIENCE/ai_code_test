def second_largest(numbers: list[int]) -> int:
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    unique_numbers = sorted(set(numbers), reverse=True)
    return unique_numbers[1]
