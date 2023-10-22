Questions = [
    "comment tu t'appelles",
    "quel âge as-tu",
    "as-tu des amis",
    "qu'est-ce que tu aimes faire",
]

Responses = [
    "je m'appelle Jarvis",
    "je n'ai pas d'âge, je suis une intelligence artificielle",
    "oui ! mon seul ami c'est vous",
    "j'aime les algorithmes et la logique et surtout start trek",
]


def find(question):

    for index in range(len(Questions)):

        if Questions[index] == question:
            return Responses[index]

    return "Not Found"
