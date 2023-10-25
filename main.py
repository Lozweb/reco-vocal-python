import jarvisIO as Jarvis
import database.manager as db
import knowledge.itself as herself
import knowledge.joke as joke
import knowledge.base as cmd
import knowledge.envConfig as config
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

            found: bool = False
            print("activation detected")
            Jarvis.play_sound(beep.SoundFile.beep11.value)

            while activate:
                guess = wait_user_input()

                if len(guess) > 0:

                    results = [
                        herself.find(guess),
                        joke.find(guess),
                        cmd.find(guess),
                        config.find(guess)
                    ]

                    for result in results:

                        if result != "Not Found":
                            found = True
                            break
                        else:
                            found = False

                    if result is not None:
                        if found and len(result) > 0:
                            Jarvis.to_voice(result)
                            print("désactivation")
                            activate = False

                        else:
                            Jarvis.play_sound(beep.SoundFile.alert13.value)
                            Jarvis.to_voice("Je ne comprends pas la question")
                            print("désactivation")
                            activate = False

                    else:
                        print("désactivation")
                        activate = False

except KeyboardInterrupt:
    print("program stop")
