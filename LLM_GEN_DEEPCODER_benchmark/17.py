from typing import List

def parse_music(music_string: str) -> List[int]:
    """Parse a string of musical notes into a list of beat durations.
    
    Args:
        music_string: A string containing musical notes separated by spaces.
                     Notes can be 'o' (whole note), 'o|' (half note), or '.|' (quarter note).
    
    Returns:
        A list of integers where each integer represents the beats of the corresponding note.
    
    Example:
        >>> parse_music('o o| .| o| o| .| .| .| .| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_to_beat = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    notes = music_string.split()
    beats = []
    for note in notes:
        if note in note_to_beat:
            beats.append(note_to_beat[note])
        else:
            raise ValueError(f"Invalid note encountered: {note}")
    return beats