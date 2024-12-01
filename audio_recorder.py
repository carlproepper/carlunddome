import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile


# Handles recording from microphone and saving audio files
def record_audio(duration=5, sample_rate=44100):
    """Record audio from microphone."""
    print(f"Recording for {duration} seconds...")
    audio_data = sd.rec(int(duration * sample_rate),
                       samplerate=sample_rate,
                       channels=1)
    sd.wait()
    print("Recording finished")
    # Convert to float32 and ensure it's in the right shape
    audio_data = audio_data.astype(np.float32)
    return audio_data.flatten()  # Flatten to 1D array

def save_audio(filename, audio_data, sample_rate=44100):
    """Save audio data to WAV file."""
    wavfile.write(filename, sample_rate, audio_data)