from typing import List

def parse_music(music_string: str) -> List[int]:
    # Define a mapping from note representation to beat value
    note_to_beats = {
        'o': 4,     # Whole note
        'o|': 2,    # Half note
        '.|': 1     # Quarter note
    }

    # Split the input music string by whitespace to get individual note representations
    tokens = music_string.split()

    # Use list comprehension to map each note to its beat value using the predefined dictionary
    beats = [note_to_beats[token] for token in tokens]

    return beats