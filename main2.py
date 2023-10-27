from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import sys
import database.manager as db
import jarvisIO
from sound import beep
import jarvisIO as Jarvis
import pyttsx3
from knowledge.base import find
import os

device_info = sd.query_devices(sd.default.device[0], 'input')
samplerate = int(device_info['default_samplerate'])
model = Model("model/vosk-model-fr-0.22/")
recognizer = KaldiRecognizer(model, samplerate)
recognizer.SetWords(False)
q = queue.Queue()

engine = pyttsx3.init()
engine.setProperty("rate", 135)
engine.setProperty("voice", "french")

db.install()


def record_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


try:

    with sd.RawInputStream(dtype='int16', channels=1, callback=record_callback):

        Jarvis.play_sound(beep.SoundFile.workbeep.value)
        Jarvis.text_to_voice(engine, "Je vous écoute")

        while True:

            guess: str
            result: str
            data = q.get()
            play_activation: bool = False

            if recognizer.AcceptWaveform(data):

                guess = jarvisIO.voice_to_text(recognizer)
                activation: bool = jarvisIO.check_user_activation(guess)
                play_activation = activation

                while activation:

                    if play_activation:
                        Jarvis.play_sound(beep.SoundFile.workbeep.value)
                        print("acitvation détecté")
                        play_activation = False

                    data = q.get()

                    if recognizer.AcceptWaveform(data):
                        guess = jarvisIO.voice_to_text(recognizer)

                        base_cmd = find(str(guess))

                        if base_cmd == "executed":
                            break

                        if len(guess) > 0:
                            response_uuid = db.search_question(str(guess))

                            if response_uuid is not None:

                                if response_uuid[0] != "Not Found":

                                    response = db.search_response(response_uuid[0])

                                    if response[0] != "Not Found":
                                        Jarvis.text_to_voice(engine, response[1])
                                        if len(response[3]) > 0:
                                            os.system(str(response[3]))

                                        activation = False

                                    else:
                                        Jarvis.text_to_voice(engine, "Une erreur s'est produite")
                                        activation = False
                                else:
                                    Jarvis.text_to_voice(engine, "Je ne sais pas")
                                    activation = False
                            else:
                                Jarvis.text_to_voice(engine, "Une erreur s'est produite pendant la recherche")
                                activation = False
                        else:
                            Jarvis.text_to_voice(engine, "Je n'ai pas compris la question")
                            activation = False


except KeyboardInterrupt:

    print('===> Finished Recording')

except Exception as e:

    print(str(e))

