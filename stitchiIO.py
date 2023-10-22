import sounddevice
import soundfile as sf
from gtts import gTTS
import audio2numpy as a2n
import speech_recognition as sr

r = sr.Recognizer()
fs = 44100
ch = 2
response_file = "./audio_temp/response.mp3"
record_file = "./audio_temp/record.wav"
keyword_activation = "Stitch"
lang = "fr-FR"
short_lang = "fr"


def record_default_device(duration, say):
    if say:
        to_voice("je vous écoutes")
    data = sounddevice.rec(int(duration * fs), samplerate=fs, channels=ch)
    sounddevice.wait()
    to_file(data, record_file)


def to_file(record, filename):
    sf.write(filename, record, fs)


def to_voice(response):
    textspeech = gTTS(text=response, lang=short_lang)
    textspeech.save(response_file)
    x, srarray = a2n.audio_from_file(response_file)
    print("Stitch : ", format(response))
    sounddevice.play(x, samplerate=fs / 1.5)
    sounddevice.wait()


def audio_to_text(filename):
    with sr.AudioFile(filename) as source:

        try:
            result = r.recognize_google(r.record(source), language=lang)
            print("Vous : ", format(result))
            return result

        except sr.UnknownValueError:
            return "Je n'ai pas compris votre question"

        except sr.RequestError as e:
            print("Error {0}".format(e))


def check_user_activation():
    with sr.AudioFile(record_file) as source:

        try:
            result = r.recognize_google(r.record(source), language=lang)

            if result == keyword_activation:
                return True
            else:
                return False

        except sr.UnknownValueError:
            return False

        except sr.RequestError as e:
            return False
