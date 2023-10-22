import sys
import os
from sound import beep
from jarvisIO import play_sound, to_voice
import webbrowser

parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)


def find(question):
    if question == "arrêt du programme":
        exit()

    elif question == "ouvre Firefox":

        try:
            webbrowser.get('firefox')
        except webbrowser.Error as e:
            give_error(str(e))

    elif question == "ouvre chrome":

        try:
            webbrowser.get(using='google-chrome')
        except webbrowser.Error as e:
            give_error(str(e))

    else:
        return "Not Found"


def give_error(error: str):
    play_sound(beep.Sound_file.alert13.value)
    to_voice(str(error), "en")
