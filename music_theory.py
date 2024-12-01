

# Helper functions for music theory operations


def note_to_freq(note_name):
    """Convert note name to frequency."""
    return librosa.note_to_hz(note_name)

def freq_to_note(frequency):
    """Convert frequency to closest note name."""
    return librosa.hz_to_note(frequency)