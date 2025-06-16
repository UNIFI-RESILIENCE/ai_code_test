from typing import List

def maxNumberOfPairs(words: List[str]) -> int:
    # Create a set to track unused words for fast lookup
    unused_words = set(words)
    pair_count = 0

    # Iterate through each word in the input list
    for word in words:
        # If word has already been used in a pair, skip it
        if word not in unused_words:
            continue

        # Compute the reverse of the current word
        reversed_word = word[::-1]

        # Ensure the pair is valid and distinct (i < j condition is inherently upheld by input)
        # Also check reversed_word is not the same as the current word (which can't be a pair due to distinct requirement)
        if reversed_word in unused_words and reversed_word != word:
            # Increment the number of pairs found
            pair_count += 1

            # Remove both words from the unused set to prevent reuse
            unused_words.remove(word)
            unused_words.remove(reversed_word)

    return pair_count