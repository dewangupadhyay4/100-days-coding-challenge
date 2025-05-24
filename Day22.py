#single level inheritance

# class Animal:
#     def speak(self):
#         print("This sound is from animal class")

# class Dog(Animal):
#     def bark(self):
#         print("This sound is from Dog")

# animal=Animal()
# animal.speak()
# dog=Dog()
# dog.bark()

#---------------------------------------------------------------------------------------

#multilevel inheritance

# class A:
#     def msgA(self):
#         print("This is A class")

# class B(A):
#     def msgB(self):
#         print("This is B class")

# class C(B):
#     def msgC(self):
#         print("This is C class")

# c=C()
# c.msgA()
# c.msgB()
# c.msgC()

#---------------------------------------------------------------------------------------

#multiple inheritance

# class Father:
#     def show_father(self):
#         print("Father class")

# class Mother:
#     def show_mother(self):
#         print("Mother class")

# class Child(Father, Mother):
#     def show_child(self):
#         print("This is child class")

# child=Child()
# child.show_father()
# child.show_mother()
# child.show_child()