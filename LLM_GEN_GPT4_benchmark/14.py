from typing import List

def all_prefixes(string: str) -> List[str]:
    # Initialize an empty list to store prefixes
    prefixes = []
    
    # Iterate over the input string using index positions
    for i in range(1, len(string) + 1):
        # Append the substring from the beginning up to index i
        prefixes.append(string[:i])
    
    # Return the completed list of prefixes
    return prefixes