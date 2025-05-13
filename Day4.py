def func(num1,num2):
    result=num1+num2
    print("The sum of numbers you entered is: ",result)

n1=int(input("Enter number one: "))
n2=int(input("Enter number two: "))
func(n1,n2)

#-------------------------------------------------------------------------------------------------------------------------------------------
def largest(nums):
    print(max(nums))

largest([23,45,12,56,222,22])

#-------------------------------------------------------------------------------------------------------------------------------------------
def even_odd(num):
    if num % 2 == 0:
        print(f"entered {num} is even")
    else:
        print(f"entered {num} is odd")

even_odd(119)

# #-------------------------------------------------------------------------------------------------------------------------------------------

def calulator(num1, num2, operation):
    if operation=='+':
        return num1+num2
    elif operation=='-':
        return num1-num2
    elif operation=='*':
        return num1*num2
    elif operation=='/':
        return num1/num2
    else:
        print("You have entered wrong input")

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
op=str(input("Enter the operation: "))
print(calulator(n1,n2,op))


