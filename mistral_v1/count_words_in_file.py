def count_words_in_file(file_path: str) -> int:
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)
