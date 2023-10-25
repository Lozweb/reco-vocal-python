import os
import sys
import sounddevice
import audio2numpy as a2n
import speech_recognition as sr
from gtts import gTTS

fs = 44100
response_file: str = "./audio_temp/response.mp3"
record_file: str = "./audio_temp/record.wav"
activate_beep: str = "./sound/computerbeep_11.mp3"
keyword_activation: str = "ordinateur"
lang: str = "fr-FR"


def record_default_device():
    print("listening...")
    audio = capture_voice_input()
    return audio_to_text(audio)


def capture_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    return audio


def to_voice(response: str, language: str = 'fr'):
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "audio_temp")):
        os.makedirs("audio_temp")

    textspeech = gTTS(text=response, lang=language)
    textspeech.save(response_file)
    x, srarray = a2n.audio_from_file(response_file)
    print(keyword_activation + " : " + response)
    sounddevice.play(x, samplerate=fs / 1.7)
    sounddevice.wait()


def audio_to_text(audio):
    try:
        r = sr.Recognizer()
        result = r.recognize_google(audio, language=lang)
        print("Vous : " + "'" + result + "'")
        return result

    except sr.UnknownValueError:
        return "Hum, je ne sais pas"

    except sr.RequestError as e:
        print("Error {0}".format(e))


def check_user_activation(result):

    if result == keyword_activation:
        return True
    else:
        return False


def play_sound(path: str):
    x, srarray = a2n.audio_from_file(path)
    sounddevice.play(x, samplerate=fs)
    sounddevice.wait()
