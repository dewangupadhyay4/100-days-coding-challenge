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

# class Calculator:
#     @staticmethod
#     def add(x, y):
#         return x + y
    
# print(Calculator.add(5,6))

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