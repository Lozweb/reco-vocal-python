Questions = [
    "comment tu t'appelles",
    "quel âge as-tu",
    "as-tu des amis",
    "qu'est-ce que tu aimes faire",
]

Responses = [
    "je m'appelle Stitch",
    "je n'ai pas d'âge, je suis une intelligence artificielle",
    "oui ! mon ami s'appelle Lilo",
    "j'aime vous écouter parler",
]


def find(question):

    for index in range(len(Questions)):

        if Questions[index] == question:
            return Responses[index]

    return "Not Found"
