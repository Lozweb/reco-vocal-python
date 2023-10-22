import record
import voice_to_text

filename = "record.wav"
text: str


def main():
    data = record.record_default_device()
    record.write_to_file(data, filename)
    return voice_to_text.translate(filename)


text = main()

if text == "comment tu t'appelles":
    print("je m'appelle Stitch")
    record.to_voice("je m'appelle Stitch")

elif text == "quel âge as-tu":
    print("je n'ai pas d'âge, je suis une intelligence artificielle")
    record.to_voice("je n'ai pas d'âge, je suis une intelligence artificielle")

elif text == "as-tu des amis":
    print("oui ! mon ami s'appelle Lilo")
    record.to_voice("oui ! mon ami s'appelle Lilo")

elif text == "qu'est-ce que tu aimes faire":
    print("j'aime vous écouter parler")
    record.to_voice("j'aime vous écouter parler")

elif text == "raconte-nous une blague":
    print("c'est l'histoire de paf le chien, il traverse la route, une voiture arrive et PAF le chien")
    record.to_voice("c'est l'histoire de paf le chien, il traverse la route, une voiture arrive et PAF le chien")

elif text == "fais-nous une devinette":

    print("qu'est ce qui est rose et qui saute de liane en liane ?")
    record.to_voice("qu'est ce qui est rose et qui saute de liane en liane ?")
    text = main()

    if text == "un malabar collé au cul de Tarzan":
        print("c'est bien ça oui")
        record.to_voice("c'est bien ça oui")
    else:
        print("un Malabar collé au cul de Tarzan")
        record.to_voice("un Malabar collé au cul de Tarzan")

else:
    print("Hum ... Je ne sais pas")
    record.to_voice("Hum ... Je ne sais pas")
