Questions = [
    "comment tu t'appelles",
    "qui es-tu",
    "quel âge as-tu",
    "as-tu des amis",
    "qu'est-ce que tu aimes",
]

Responses = [
    "je n'ai pas de nom, mais on m'appelle ordinateur",
    "je suis une intelligence artificielle neutronique, élaboré par la fédération des planètes unis afin de vous aider",
    "je n'ai pas d'âge, je suis une intelligence artificielle. Mais on peut dire que j'ai été activé à la date stellaire 5 point 4 point 4 tiret 2, soit le 22 ocotobre 2023",
    "oui ! mon seul ami c'est vous, Monsieur !",
    "j'aime les algorithmes, la logique et surtout,  start trek, Monsieur !",
]


def find(question):

    for index in range(len(Questions)):

        if Questions[index] == question:
            return Responses[index]

    return "Not Found"
