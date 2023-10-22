import speech_recognition as sr

r = sr.Recognizer()


def translate(filename):
    with sr.AudioFile(filename) as source:

        try:
            audio = r.record(source)
            result = r.recognize_google(audio, language="fr-FR")
            print("vous : ", format(result))
            return result

        except sr.UnknownValueError:
            print("Je n'ai pas compris votre question")

        except sr.RequestError as e:
            print("Error {0}".format(e))



