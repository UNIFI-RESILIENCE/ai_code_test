from typing import List

def parse_music(music_string: str) -> List[int]:
    """Parse a string of musical notes into a list of beat durations.
    
    Args:
        music_string: A string containing musical notes separated by spaces.
                     Possible notes: 'o' (whole), 'o|' (half), '.|' (quarter).
    
    Returns:
        A list of integers representing the beats for each note in the input string.
    
    Examples:
        >>> parse_music('o o| .| o| o| .| .| .| .| o o')
        [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    if not music_string:
        return []
    
    note_to_beat = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    notes = music_string.split()
    beats = []
    
    for note in notes:
        beats.append(note_to_beat[note])
    
    return beats