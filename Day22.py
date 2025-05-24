#single level inheritance

class Animal:
    def speak(self):
        print("This sound is from animal class")

class Dog(Animal):
    def bark(self):
        print("This sound is from Dog")

animal=Animal()
animal.speak()
dog=Dog()
dog.bark()