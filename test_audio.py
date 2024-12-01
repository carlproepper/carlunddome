import pytest
import numpy as np
from audio.recorder import record_audio, save_audio
from audio.audio_processor import preprocess_audio

# Basic tests for audio functionality


def test_audio_recording():
    """Test audio recording."""
    audio = record_audio(duration=1)
    assert isinstance(audio, np.ndarray)
    assert len(audio) > 0

def test_preprocessing():
    """Test audio preprocessing."""
    test_audio = np.random.rand(44100)
    processed = preprocess_audio(test_audio)
    assert np.max(np.abs(processed)) <= 1.0