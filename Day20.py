class Person:
    def __init__(self, name):
        self.name=name

    def greet(self):
        print(f"Hello this is {self.name}")

person=Person("Dewang")
person.greet()

#---------------------------------------------------------------------------

class Employee:
    company="Tata Capital"

    @classmethod
    def show_company(cls):
        print(f"We work at {cls.company}")

Employee.show_company()

#---------------------------------------------------------------------------

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
    
print(Calculator.add(5,6))

#---------------------------------------------------------------------------

class Student:
    school="Trinity"

    def __init__(self,name, age):
        self.name=name
        self.age=age

    def show_student(self):
        print(f"Hello {self.name} and age is {self.age}")

    @classmethod
    def school_name(cls):
        print(f"School name is {cls.school}")

    @staticmethod
    def is_adult(age):
        if age >= 18:
            return "adult"
        
student=Student("dewang", 22)
student.show_student()

Student.school_name()

print(Student.is_adult(21))

#---------------------------------------------------------------------------------------------------

# 🔹 1. Instance Method
# Defined with: def method_name(self)
# Accesses: Instance (self) → instance variables and methods
# Called by: An object (instance) of the class
# Use Case: When you need to access or modify object-specific data

# 🔹 2. Class Method
# Defined with: @classmethod and def method_name(cls)
# Accesses: Class (cls) → class variables and methods
# Called by: Class or object
# Use Case: When you want to access or modify class-level data

# 🔹 3. Static Method
# Defined with: @staticmethod and def method_name()
# Accesses: Neither class (cls) nor instance (self)
# Called by: Class or object
# Use Case: Utility functions that don’t depend on class or instance data