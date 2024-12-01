import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile
import librosa
import pretty_midi
import time
import os
def record_audio(duration=5, sample_rate=44100):
    print("Get ready to hum...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Start humming!")

    audio_data = sd.rec(int(duration * sample_rate),
                        samplerate=sample_rate,
                        channels=1)
    sd.wait()
    print("Recording finished!")
    return audio_data.astype(np.float32).flatten()


def process_audio(audio_data, sample_rate=44100):
    # Normalize
    audio_data = audio_data / np.max(np.abs(audio_data) + 1e-10)
    return audio_data


def detect_notes(audio_data, sample_rate=44100):
    # Detect pitches
    pitches, magnitudes = librosa.piptrack(y=audio_data,
                                           sr=sample_rate,
                                           fmin=librosa.note_to_hz('C2'),
                                           fmax=librosa.note_to_hz('C7'))

    # Get the strongest pitch at each time
    notes = []
    current_time = 0
    hop_time = 512 / sample_rate  # librosa default hop length

    for time_idx in range(pitches.shape[1]):
        pitch_idx = magnitudes[:, time_idx].argmax()
        pitch = pitches[pitch_idx, time_idx]
        if pitch > 0:  # if pitch detected
            notes.append({
                'pitch': pitch,
                'start': current_time,
                'duration': hop_time
            })
        current_time += hop_time

    return notes


def create_midi(notes, output_file="test_melody.mid"):
    pm = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=0)  # Piano

    for note in notes:
        if note['pitch'] > 0:  # Valid pitch
            note_number = pretty_midi.hz_to_midi_note_number(note['pitch'])
            note = pretty_midi.Note(
                velocity=100,
                pitch=int(note_number),
                start=note['start'],
                end=note['start'] + note['duration']
            )
            piano.notes.append(note)

    pm.instruments.append(piano)
    pm.write(output_file)
    return output_file


def create_audio_file(notes, output_file="output/melody.wav", sample_rate=44100):
    # Convert MIDI to audio using pretty_midi
    pm = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=0)

    for note in notes:
        if note['pitch'] > 0:
            note_number = pretty_midi.hz_to_midi_note_number(note['pitch'])
            note = pretty_midi.Note(
                velocity=100,
                pitch=int(note_number),
                start=note['start'],
                end=note['start'] + note['duration']
            )
            piano.notes.append(note)

    pm.instruments.append(piano)

    # Synthesize audio
    audio_data = pm.synthesize()

    # Save as WAV file
    wavfile.write(output_file, sample_rate, audio_data)
    return output_file

# Create output directory
os.makedirs("output", exist_ok=True)

# Record
print("Recording 5 seconds of audio...")
audio = record_audio(5)

# Process
print("Processing audio...")
processed_audio = process_audio(audio)

# Detect notes
print("Detecting notes...")
notes = detect_notes(processed_audio)

# Create MIDI
print("Creating MIDI file...")
midi_file = create_midi(notes, "output/test_melody.mid")

print(f"MIDI file created: {midi_file}")
print("You can now open this file with your favorite MIDI player!")

audio_file = create_audio_file(notes, "output/melody.wav")
print(f"Audio file created: {audio_file}")

