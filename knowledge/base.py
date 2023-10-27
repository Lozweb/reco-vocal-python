import sys
import os
from sound import beep
from jarvisIO import play_sound, to_voice, record_default_device
import database.manager as db

parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)


def find(question):
    if question == "arrêt du programme" or question == "fin du programme":
        exit()

    elif question == "ajouter une compétence" or question == "ajoute une compétence":
        add_skill()

    else:
        return "Not Found"

    return "executed"


def give_error(error: str):
    play_sound(beep.SoundFile.alert13.value)
    to_voice(str(error), "en")


def add_skill():
    guess: str
    qs: str
    rs: str
    ty: str
    cmd: str

    while True:
        to_voice("Voulez-vous dictée la question ou l'écrire ?")
        guess = record_default_device()

        if guess == "dictée":
            to_voice("Énoncez la question")
            play_sound(beep.SoundFile.beep11.value)
            qs = record_default_device()
            break

        elif guess == "écrire":
            print("Entrez la question")
            qs = input()
            break

        else:
            continue

    while True:
        to_voice("Voulez-vous dictée la réponse ou l'écrire ?")
        guess = record_default_device()

        if guess == "dictée":
            to_voice("Énoncez la réponse")
            play_sound(beep.SoundFile.beep11.value)
            rs = record_default_device()
            break

        elif guess == "écrire":
            print("Entrez la réponse")
            rs = input()
            break

        else:
            continue

    while True:
        to_voice("Voulez-vous dictée le type de retour ou l'écrire ?")
        guess = record_default_device()

        if guess == "dictée":
            to_voice("Le type de retour sera une question ou une réponse ?")
            play_sound(beep.SoundFile.beep11.value)
            ty = record_default_device()
            break

        elif guess == "écrire":
            print("Entrez le type de retour")
            ty = input()
            break

        else:
            continue

    while True:
        to_voice("Voulez-vous qu'une commande soit executé avec la réponse ?")
        guess = record_default_device()

        if guess == "oui":
            to_voice("écrivez la commande bash dans votre terminal")
            cmd = input()
            break

        elif guess == "non":
            cmd = ""
            break

        else:
            continue

    db.create_question(qs, rs, ty, cmd)
    to_voice("la compétence a été ajoutée")


