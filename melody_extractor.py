import numpy as np

# Combines pitch and onset data to create melody

def extract_melody(pitches, onsets):
    """Convert pitch and onset data to melody."""
    melody = []
    for i in range(len(onsets) - 1):
        # Get average pitch between onsets
        start_idx = int(onsets[i] * len(pitches))
        end_idx = int(onsets[i + 1] * len(pitches))
        pitch = np.mean(pitches[start_idx:end_idx])
        duration = onsets[i + 1] - onsets[i]
        melody.append({'pitch': pitch, 'duration': duration})
    return melody