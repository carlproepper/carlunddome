import librosa
import numpy as np

# Implements pitch detection algorithm

def detect_pitch(audio_data, sample_rate=44100):
    """Detect pitch from audio data."""
    if np.all(audio_data == 0):
        return np.array([])

    pitches, magnitudes = librosa.piptrack(
        y=audio_data,
        sr=sample_rate,
        fmin=librosa.note_to_hz('C2'),
        fmax=librosa.note_to_hz('C7')
    )

    # Get the most prominent pitch at each time
    pitch_values = []
    for time_idx in range(pitches.shape[1]):
        index = magnitudes[:, time_idx].argmax()
        pitch_values.append(pitches[index, time_idx])

    return np.array(pitch_values)