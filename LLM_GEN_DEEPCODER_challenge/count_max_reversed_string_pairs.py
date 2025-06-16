def maximumNumberOfStringPairs(words):
    """
    Calculate the maximum number of pairs in the given list of words
    where one word is the reverse of another and each word is used at most once.

    Args:
    words: A list of distinct strings of length 2.

    Returns:
    int: The maximum number of pairs that can be formed.
    """
    word_set = set()
    count = 0
    
    for word in words:
        reversed_word = word[::-1]
        if reversed_word in word_set:
            count += 1
            word_set.remove(reversed_word)
        else:
            word_set.add(word)
    
    return count

# Example usage
if __name__ == "__main__":
    print(maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))  # Output: 2
    print(maximumNumberOfStringPairs(["ab","ba","cc"]))            # Output: 1
    print(maximumNumberOfStringPairs(["aa","ab"]))                 # Output: 0