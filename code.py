import datetime

class EnglishClass:
    def __init__(self, name):
        self.name = name
        self.welcome_guest()

    def welcome_guest(self):
        print(f"Hello {self.name}, welcome!")


class FrenchClass(EnglishClass):
    def welcome_guest(self):
        print(f"Bonjour {self.name}, bienvenue!")


class GermanClass:
    def welcome_guest(self):
        print(f"Hallo {self.name}, willkommen!")


class SpanishClass(EnglishClass):
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def welcome_guest(self):
        if datetime.date.today() == self.birthday:
            print(f"Hola {self.name} feliz cumpleaños")
        else:
            print(f"Hola {self.name}, bienvenido")


if __name__ == "__main__":
    name = "James"
    # What will each of these do?
    english = EnglishClass(name)

    print(english.name)

    FrenchClass(name)

    GermanClass(name)

    SpanishClass(name, datetime.date(2019, 7, 26))
