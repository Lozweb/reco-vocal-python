import stitchiIO as Stitch
import stitch_knowledge.herself as herself
import stitch_knowledge.joke as joke
import stitch_knowledge.base as cmd

filename = "./audio_temp/record.wav"


def wait_user_input():
    return Stitch.record_default_device(True)


def wait_user_activation():
    keyword = Stitch.record_default_device(False)
    return Stitch.check_user_activation(keyword)


try:

    while True:

        guess: str
        result: str = ""
        found: bool = False
        activate: bool = wait_user_activation()

        if activate:
            print("activation detected")

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

                    if found and len(result) > 0:
                        Stitch.to_voice(result)
                        activate = False

                    else:
                        if len(guess) > 0:
                            print(guess)
                        Stitch.to_voice("Je n'ai pas compris votre question")
                        activate = False

except KeyboardInterrupt:
    print("program stop")
