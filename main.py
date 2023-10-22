import jarvisIO as Jarvis
import stitch_knowledge.itself as herself
import stitch_knowledge.joke as joke
import stitch_knowledge.base as cmd
from sound import beep


def wait_user_input():
    return Jarvis.record_default_device()


def wait_user_activation():
    keyword = Jarvis.record_default_device()
    return Jarvis.check_user_activation(keyword)


try:

    while True:

        Jarvis.play_sound(beep.Sound_file.workbeep.value)

        guess: str
        result: str = ""
        found: bool = False
        activate: bool = wait_user_activation()

        if activate:

            print("activation detected")
            Jarvis.play_sound(beep.Sound_file.beep11.value)

            while activate:
                guess = wait_user_input()

                if len(guess) > 0:

                    results = [
                        herself.find(guess),
                        joke.find(guess),
                        cmd.find(guess)
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
                            activate = False

                        else:
                            Jarvis.play_sound(beep.Sound_file.alert13.value)
                            Jarvis.to_voice("Je ne comprends pas la question")
                            activate = False

                    else:
                        activate = False

except KeyboardInterrupt:
    print("program stop")
