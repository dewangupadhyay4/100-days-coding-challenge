#inheritance
# class Employee:
#     def works(self):
#         print("This is Employee class")

# class Manager(Employee):
#     def works(self):
#         print("This is Manager class")

# employee=Employee()
# employee.works()

# manager=Manager()
# manager.works()

#---------------------------------------------------------

#Encapsulation

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand=brand
#         self.__model=model
#         self.__year=year

#     def get_car(self):
#         return self.__model
    
#     def get_details(self):
#         print(f"The car brand is {self.brand} , model is {self.__model} and year is {self.__year}")

# car= Car("Maruti","ABCS",2021)
# print(car.get_car())

# car.get_details()

#---------------------------------------------------------

class Bird:
    def fly(self):
        print("This is bird flying in bird class")

class Airplane:
    def fly(self):
        print("This is airplane flying in airplane class")

for i in (Bird(), Airplane()):
    i.fly()