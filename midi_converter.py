import pretty_midi

# Converts melody to MIDI format

def convert_to_midi(melody, tempo=120):
    """Convert melody data to MIDI format."""
    pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)
    piano = pretty_midi.Instrument(program=0)  # Piano

    current_time = 0.0
    for note in melody:
        note_number = librosa.hz_to_midi(note['pitch'])
        note = pretty_midi.Note(
            velocity=100,
            pitch=int(note_number),
            start=current_time,
            end=current_time + note['duration']
        )
        piano.notes.append(note)
        current_time += note['duration']

    pm.instruments.append(piano)
    return pm