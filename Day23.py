class Person:
    def work(self):
        print("person works")

class Teacher(Person):
    def work(self):
        print("Teacher works")

class Engineer(Person):
    def work(self):
        print("Engineer works")

for i in (Person(), Teacher(), Engineer()):
    print(i.work())

print()

jobs=[Person(), Teacher(), Engineer()]
for i in jobs:
    i.work()