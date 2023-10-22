import speech_recognition as sr

recognizer = sr.Recognizer()


def capture_voice_input():
    with sr.Microphone() as source:
        print("listening")
        audio = recognizer.listen(source)
    return audio


def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio, language='fr-FR')
        return text
    except sr.UnknownValueError:
        return "j'ai pas compris"
    except sr.RequestError:
        return "error"


def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        print(text)
        end_program = True


main()