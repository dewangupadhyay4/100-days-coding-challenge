# class Person:
#     def __init__(self, name):
#         self.name=name

#     def greet(self):
#         print(f"Hello this is {self.name}")

# person=Person("Dewang")
# person.greet()

#---------------------------------------------------------------------------

# class Employee:
#     company="Tata Capital"

#     @classmethod
#     def show_company(cls):
#         print(f"We work at {cls.company}")

# Employee.show_company()

#---------------------------------------------------------------------------

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
    
print(Calculator.add(5,6))