class Registeration:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def regis(self):
        print(f"Hii my name is {self.name} and I am {self.age} years old")

registeration=Registeration("dewang",21)
registeration.regis()

#----------------------------------------------------------------------------------------------------

class Car:
    def __init__(self, brand, model, year):
        self.brand=brand
        self.model=model
        self.year=year

    def show_details(self):
        print(f"This is {self.brand} and model is {self.model} which was built in {self.year}")

car=Car("Tesla", "Model 3", 2023)
car.show_details()
