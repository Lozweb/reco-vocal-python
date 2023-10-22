import sounddevice as sd
import soundfile as sf
from gtts import gTTS
import audio2numpy as a2n

duration = 2
fs = 44100
ch = 2


def record_default_device():
    # Record start
    print("Je vous écoute")
    record = sd.rec(int(duration * fs), samplerate=fs, channels=ch)
    sd.wait()
    # Record End
    return record


def write_to_file(record, filename):
    sf.write(filename, record, fs)


def to_voice(response):
    textspeech = gTTS(text=response, lang='fr')
    textspeech.save("response.mp3")
    x, sr = a2n.audio_from_file("response.mp3")
    sd.play(x, samplerate=fs/1.5)
    sd.wait()
