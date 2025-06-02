# Open the file in read mode
with open("file.txt", "r") as file:
    # Read the contents of the file
    text = file.read()

# Split the text into words using whitespace as the delimiter
words = text.split()

# Count the number of words
num_words = len(words)

# Print the result
print(f"The text file contains {num_words} words.")