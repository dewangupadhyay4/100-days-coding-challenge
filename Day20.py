class Person:
    def __init__(self, name):
        self.name=name

    def greet(self):
        print(f"Hello this is {self.name}")

person=Person("Dewang")
person.greet()