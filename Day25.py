#1. Encapsulation – Bundling data and methods into a class and restricting direct access.

class Person:
    def __init__(self):
        self.__age = 25  # private variable

    def get_age(self):
        return self.__age

#2. Inheritance – One class inherits properties and methods from another.

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    pass

#3. Polymorphism – Same method name behaves differently in different classes.

class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

for animal in (Dog(), Cat()):
    animal.sound()

#4. Abstraction – Hiding implementation and showing only necessary details.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# What is the use of the @abstractmethod decorator?

# a) To define a private method

# b) To define a static method

# c) To define a method that must be implemented by child classes

# d) None of the above

# What will happen if you try to instantiate an abstract class?

# a) It works normally

# b) SyntaxError

# c) RuntimeError

# d) TypeError

# Which OOP principle is used when we override a method in a subclass?

# a) Encapsulation

# b) Abstraction

# c) Polymorphism

# d) Inheritance

# What is the correct way to make a variable private in Python?

# a) private age

# b) __age

# c) age__

# d) _private age

# Which concept restricts direct access to variables and methods?

# a) Abstraction

# b) Polymorphism

# c) Encapsulation

# d) Inheritance