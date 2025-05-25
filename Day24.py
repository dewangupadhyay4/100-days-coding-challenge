from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meows")

animal=Animal()
animal.make_sound() #will raise error