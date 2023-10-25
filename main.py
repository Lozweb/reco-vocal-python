import jarvisIO as Jarvis
import database.manager as db
from sound import beep
from knowledge.base import find
import os

db.install()


def wait_user_input():
    return Jarvis.record_default_device()


def wait_user_activation():
    keyword = Jarvis.record_default_device()
    return Jarvis.check_user_activation(keyword)


try:

    Jarvis.play_sound(beep.SoundFile.workbeep.value)

    while True:
        guess: str
        result: str = ""
        activate: bool = wait_user_activation()

        if activate:
            print("activation detected")
            Jarvis.play_sound(beep.SoundFile.beep11.value)

            while activate:
                guess = wait_user_input()
                activate = False

                base_cmd = find(str(guess))
                if base_cmd == "executed":
                    break

                if len(guess) > 0:
                    response_uuid = db.search_question(str(guess))

                    if response_uuid is not None:

                        if response_uuid[0] != "Not Found":

                            response = db.search_response(response_uuid[0])

                            if response[0] != "Not Found":
                                Jarvis.to_voice(response[1])
                                if len(response[3]) > 0:
                                    os.system(str(response[3]))

                            else:
                                Jarvis.to_voice("Une erreur s'est produite")
                        else:
                            Jarvis.to_voice("Je ne sais pas")
                    else:
                        Jarvis.to_voice("Une erreur s'est produite pendant la recherche")
                else:
                    Jarvis.to_voice("Je n'ai pas compris la question")

except KeyboardInterrupt:
    print("program stop")
