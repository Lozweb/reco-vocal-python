import sounddevice
from gtts import gTTS
import audio2numpy as a2n
import speech_recognition as sr

r = sr.Recognizer()
fs = 44100
response_file = "./audio_temp/response.mp3"
record_file = "./audio_temp/record.wav"
keyword_activation = "Jarvis"
lang = "fr-FR"
short_lang = "fr"


def record_default_device(say):
    if say:
        to_voice("je vous écoutes")
    print("listening...")
    audio = capture_voice_input()
    return audio_to_text(audio)


def capture_voice_input():
    with sr.Microphone() as source:
        audio = r.listen(source)
    return audio


def to_voice(response):
    textspeech = gTTS(text=response, lang=short_lang)
    textspeech.save(response_file)
    x, srarray = a2n.audio_from_file(response_file)
    print("Stitch : ", format(response))
    sounddevice.play(x, samplerate=fs / 1.5)
    sounddevice.wait()


def audio_to_text(audio):
    try:
        result = r.recognize_google(audio, language=lang)
        print("Vous : ", format(result))
        return result

    except sr.UnknownValueError:
        return "Je n'ai pas compris votre question"

    except sr.RequestError as e:
        print("Error {0}".format(e))


def check_user_activation(result):

    if result == keyword_activation:
        return True
    else:
        return False
