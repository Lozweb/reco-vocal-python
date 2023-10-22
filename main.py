import stitchiIO as Stitch
import stitch_knowledge.herself as herself
import stitch_knowledge.joke as joke
import stitch_knowledge.base as cmd

filename = "./audio_temp/record.wav"


def wait_user_input():
    Stitch.record_default_device(4, True)
    return Stitch.audio_to_text(filename)


def wait_user_activation():
    Stitch.record_default_device(2, False)
    return Stitch.check_user_activation()


try:

    while True:

        guess: str
        result: str = ""
        found: bool = False
        activate: bool = wait_user_activation()

        if activate:
            print("activation detected")
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
                    Stitch.to_voice("Je n'ai pas compris votre question")
                    activate = False

except KeyboardInterrupt:
    print("program stop")
