from typing import List

def parse_music(music_string: str) -> List[int]:
    # Split the input string into individual note representations
    notes = music_string.split()

    # Initialize an empty list to store the duration (beats) of each note
    beats = []

    # Iterate over each note in the parsed list
    for note in notes:
        # Determine the duration of each note based on the provided legend
        if note == 'o':
            # Whole note, lasts four beats
            beats.append(4)
        elif note == 'o|':
            # Half note, lasts two beats
            beats.append(2)
        elif note == '.|':
            # Quarter note, lasts one beat
            beats.append(1)
        else:
            # Handle unexpected note representation
            raise ValueError(f"Unexpected note representation: {note}")

    # Return the list of beats corresponding to each note
    return beats