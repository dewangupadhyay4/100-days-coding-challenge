age=int(input("Enter your age to check if you are eligible to vote or not: "))

if age>=18 and age<100:
    print("Yess!!! Your are eligible to vote")
elif age<18 and age>1:
    print("No!!! You are not eligible to vote")
else:
    print("You have entered incorrect age")

#--------------------------------------------------------------------------------------------------------------------------------------------------

# num=int(input("Enter number to get to know wheter it is positive , negative , zero"))
# if num==0:
#     print("You have entered 0")
# elif num > 0:
#     print("Number is Positive")
# elif num < 0:
#     print("Number is Negative")
# else:
#     print("Incorrect entry")

#---------------------------------------------------------------------------------------------------------------------------------------------------
# username=str(input("Enter your username: "))
# if username == 'dewang22':
#     password=str(input("Enter your password: "))
#     if password == 'dew123' or password=='dew':
#         print("Login successful")
#     else:
#         print("Password is incorrect")
# else:
#     print("Username is incorrect")