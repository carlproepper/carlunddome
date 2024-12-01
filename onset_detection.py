import librosa
import numpy as np

# Detects when new notes begin


def detect_onsets(audio_data, sample_rate=44100):
    """Detect note onsets in audio."""
    onset_frames = librosa.onset.onset_detect(
        y=audio_data,
        sr=sample_rate,
        wait=5,
        pre_avg=3,
        post_avg=3,
        pre_max=3,
        post_max=3
    )

    onset_times = librosa.frames_to_time(onset_frames, sr=sample_rate)
    return onset_times