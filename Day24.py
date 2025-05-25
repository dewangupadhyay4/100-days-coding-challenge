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

# animal=Animal()
# animal.make_sound() #will raise error

dog=Dog()
cat=Cat()

dog.make_sound()
cat.make_sound()

#-------------------------------------------------------------------------------------------------------------------

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        print("Here printing area of rectangle")

class Circle(Shape):
    def area(self):
        print("Here printing the area of the circle")

rectangle=Rectangle()
circle=Circle()
rectangle.area()
circle.area()