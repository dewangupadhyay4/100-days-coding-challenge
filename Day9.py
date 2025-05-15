def add():
    print("Hello this function is just for calling purpose")

add()  #calling add funtion

#-----------------------------------------------------------------------------------

def adding_function(num1, num2): #num1 and num2 are parameters
    return num1+num2

print(adding_function(5,8)) #5,8 are arguments

#-----------------------------------------------------------------------------------------------------

def another_addition(*args):
    total=0
    for i in args:
        total += i
    return total

print(another_addition(45,5,3))

#-----------------------------------------------------------------------------------------------------

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="dewang", age=22, city="Mumbai")