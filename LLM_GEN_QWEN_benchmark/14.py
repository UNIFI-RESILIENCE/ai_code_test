from typing import List

def all_prefixes(string: str) -> List[str]:
    # Initialize an empty list to store the prefixes
    prefixes = []
    
    # Iterate over the length of the string to get each prefix
    for i in range(1, len(string) + 1):
        # Append the substring from the start to the ith index
        prefixes.append(string[:i])
    
    # Return the list of prefixes
    return prefixes

# Example usage:
# result = all_prefixes('abc')
# print(result)  # Output: ['a', 'ab', 'abc']