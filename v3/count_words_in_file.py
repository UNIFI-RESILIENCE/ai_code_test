# Open the file in read mode
with open('filename.txt', 'r') as file:
    # Read all lines in the file
    content = file.read()

# Split the content into words using whitespace as the delimiter
words = content.split()

# Count the number of words
num_words = len(words)

# Print the result
print(f'The number of words in the file is: {num_words}')