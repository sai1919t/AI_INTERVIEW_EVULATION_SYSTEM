import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

def record_audio_until_silence(filename, fs=44100, silence_threshold=0.01, silence_duration=3):

    print("Recording... Speak now")

    recording = []
    silence_counter = 0

    def callback(indata, frames, time, status):
        nonlocal silence_counter

        volume = np.linalg.norm(indata)

        recording.append(indata.copy())

        if volume < silence_threshold:
            silence_counter += 1
        else:
            silence_counter = 0

        if silence_counter > silence_duration * 10:
            raise sd.CallbackStop()

    try:
        with sd.InputStream(callback=callback):
            sd.sleep(60000)  # max 60 sec limit
    except:
        pass

    audio = np.concatenate(recording)
    write(filename, fs, audio)

    print("Answer recording finished.")