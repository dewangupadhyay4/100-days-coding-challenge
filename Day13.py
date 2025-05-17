# try:
#     num=int(input("Enter a number"))
#     result=num/0
# except ZeroDivisionError:
#     print("Number cannot be divided by 0")
# except ValueError:
#     print("Please enter a valid number")

#--------------------------------------------------------------------------------

# try:
#     name=input("Enter the name: ")
#     print(f"You have entered {name}")
# except Exception as e:
#     print(e)

#----------------------------------------------------------------------------------

# try:
#     num=int(input("Enter the number: "))
#     result=num/0
# except ZeroDivisionError:
#     print("number cannot be divide by 0")
# finally:
#     print("This is finally block and this will execute everytime")

#----------------------------------------------------------------------------------

age=int(input("Enter the age: "))
if age <0:
    raise ValueError("You have entered wrong input")