class Vehicle:
    def describe(self):
        print("this statement is from vehicle class")

class Car(Vehicle):
    def describe(self):
        print("This is from car class")

class Bike(Vehicle):
    def describe(self):
        print("This is from Bike class")

class Bus(Vehicle):
    def describe(self):
        print("This is Bus class")

for i in (Car(),Bike(), Bus()):
    i.describe()