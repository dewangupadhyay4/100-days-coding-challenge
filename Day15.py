#inheritance
class Employee:
    def works(self):
        print("This is Employee class")

class Manager(Employee):
    def works(self):
        print("This is Manager class")

employee=Employee()
employee.works()

manager=Manager()
manager.works()