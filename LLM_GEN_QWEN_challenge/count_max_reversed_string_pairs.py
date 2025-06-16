def maximum_pairs(words):
    # Initialize a set to store the reversed words we have seen so far
    reversed_words_seen = set()
    # Initialize a counter to count the number of valid pairs
    pair_count = 0
    
    # Iterate through each word in the words list
    for word in words:
        # Generate the reversed version of the current word
        reversed_word = word[::-1]
        
        # Check if this reversed word has been seen before
        if reversed_word in reversed_words_seen:
            # If it has been seen, increment the pair count
            pair_count += 1
        else:
            # Otherwise, add the current word to the set (in reversed form)
            reversed_words_seen.add(word)

    # Return the total number of pairs found
    return pair_count

# Example usage:
words1 = ["cd", "ac", "dc", "ca", "zz"]
words2 = ["ab", "ba", "cc"]
words3 = ["aa", "ab"]

print(maximum_pairs(words1))  # Output: 2
print(maximum_pairs(words2))  # Output: 1
print(maximum_pairs(words3))  # Output: 0