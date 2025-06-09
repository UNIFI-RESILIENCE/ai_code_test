from typing import List

def parse_music(music_string: str) -> List[int]:
    # Mapping of musical note strings to their corresponding beat count
    beat_mapping = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }

    # Split the input string into individual note tokens
    notes = music_string.split()
    
    # Convert each note to its corresponding beat using the mapping
    beats = [beat_mapping[note] for note in notes if note]

    return beats

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):
    assert candidate('') == []
    assert candidate('o o o o') == [4, 4, 4, 4]
    assert candidate('.| .| .| .|') == [1, 1, 1, 1]
    assert candidate('o| o| .| .| o o o o') == [2, 2, 1, 1, 4, 4, 4, 4]
    assert candidate('o| .| o| .| o o| o o|') == [2, 1, 2, 1, 4, 2, 4, 2]