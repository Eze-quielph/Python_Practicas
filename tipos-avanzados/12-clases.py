# Classes #

class MyPerson:
    pass


class Person:     # Constructor
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def walk(self):
        print(f"{self.name} hello")
