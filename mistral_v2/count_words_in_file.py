def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage
file_path = 'sample.txt'
word_count = count_words(file_path)
print(f"The number of words in the file is: {word_count}")