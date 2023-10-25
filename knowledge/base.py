import sys
import os
from sound import beep
from jarvisIO import play_sound, to_voice, record_default_device
import webbrowser
import database.manager as db

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

    elif question == "ajouter une compétence":
        add_skill()

    else:
        return "Not Found"


def give_error(error: str):
    play_sound(beep.SoundFile.alert13.value)
    to_voice(str(error), "en")


def add_skill():

    to_voice("Énoncez la question")
    play_sound(beep.SoundFile.beep11.value)
    qs = record_default_device()

    to_voice("Énoncez la réponse")
    play_sound(beep.SoundFile.beep11.value)
    rs = record_default_device()

    to_voice("Le type de retour sera une question ou une réponse ?")
    play_sound(beep.SoundFile.beep11.value)
    ty = record_default_device()

    db.create_question(qs, rs, ty, "")
    to_voice("la compétence a été ajoutée")
