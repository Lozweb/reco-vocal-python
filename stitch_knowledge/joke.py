Guess = [
    "raconte-moi une blague",
    "fais-moi une devinette",
]

Joke = [
    "c'est l'histoire de paf le chien, il traverse la route, une voiture arrive et PAF le chien",
    "c'est l'histoire de flap flap la girafe, elle est dans la savane, un hélicoptère arrive et flap flap la giraf",
]

Ridle = [
    "qu'est ce qui est rose et qui saute de liane en liane ?",
    "qu'est ce qui est rose jaune et qui attend ?",
]


def find(question):

    for index in range(len(Guess)):

        if Guess[index] == question:

            if index == 0:
                # add random value between enum length
                return Joke[0]

            elif index == 1:
                # add random value between enum length
                return Ridle[0]

            else:
                return "Not Found"

    return "Not Found"
