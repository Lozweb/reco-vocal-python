import jarvisIO as Jarvis
import database.manager as db
from sound import beep

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

                if len(guess) > 0:

                    response_uuid = db.search_question(str(guess))

                    if response_uuid is not None:

                        response = db.search_response(response_uuid[0])
                        Jarvis.to_voice(response[1])

                    else:
                        Jarvis.to_voice("Je n'ai pas trouvé de correspondance")
                        activate = False

                else:
                    Jarvis.to_voice("Je n'ai pas compris la question")
                    activate = False


except KeyboardInterrupt:
    print("program stop")
