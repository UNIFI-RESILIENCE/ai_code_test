Here's the optimum implementation of the parse_music function based on the problem description:

from typing import List

def parse_music(music_string: str) -> List[int]:
    """Parses a music string and returns a list of beat durations for each note."""
    # Mapping of note notation to beats
    note_to_beats = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }

    # Split the input string into individual note tokens
    if not music_string.strip():
        return []

    notes = music_string.split()
    return [note_to_beats[note] for note in notes]