from typing import List

def parse_music(music_string: str) -> List[int]:
    # Define a dictionary to map note representations to their beat values
    note_to_beats = {
        'o': 4,    # whole note
        'o|': 2,   # half note
        '.|': 1    # quarter note
    }
    
    # Split the input string by spaces to get individual note representations
    notes = music_string.split()
    
    # Map each note representation to its corresponding beat value using the dictionary
    beats = [note_to_beats[note] for note in notes]
    
    return beats

# Metadata dictionary (not used in the function but provided in the prompt)
METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

# Function to check the correctness of the parse_music function
def check(candidate):
    assert candidate('') == [], "Test case for empty string failed"
    assert candidate('o o o o') == [4, 4, 4, 4], "Test case for four whole notes failed"
    assert candidate('.| .| .| .|') == [1, 1, 1, 1], "Test case for four quarter notes failed"
    assert candidate('o| o| .| .| o o o o') == [2, 2, 1, 1, 4, 4, 4, 4], "Test case for mixed notes failed"
    assert candidate('o| .| o| .| o o| o o|') == [2, 1, 2, 1, 4, 2, 4, 2], "Test case for mixed notes failed"

# Uncomment the line below to run the checks
# check(parse_music)