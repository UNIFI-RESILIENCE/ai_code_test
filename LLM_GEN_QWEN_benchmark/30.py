def get_positive(lst: list) -> list:
    # Use a list comprehension to filter out positive numbers from the list
    return [num for num in lst if num > 0]