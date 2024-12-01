import numpy as np
import librosa

# Handles audio preprocessing and cleaning

def preprocess_audio(audio_data, sample_rate=44100):
    """Clean and normalize audio data."""
    # Check for zero array
    if np.all(audio_data == 0):
        return audio_data

    # Normalize
    audio_normalized = audio_data / np.max(np.abs(audio_data) + 1e-10)  # Add small number to prevent division by zero

    return audio_normalized

