import webbrowser


def find(question):

    if question == "stoppe":
        exit()

    elif question == "ouvre Firefox":

        try:
            webbrowser.get('firefox')
        except webbrowser.Error as e:
            print(e)

    elif question == "ouvre chrome":

        try:
            webbrowser.get(using='google-chrome')
        except webbrowser.Error as e:
            print(e)

    else:
        return "Not Found"
