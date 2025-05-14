num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

if num1 == num2 == num3:
    print("All the numbers are equal")
else:
    if num1 >= num2 and num1 >= num3:
        print(f"Largest number is : {num1}")
    elif num2 >= num1 and num2 >= num3:
        print(f"Largest number is : {num2}")
    else:
        print(f"Largest number is : {num3}")

    if num1 <= num2 and num1 <= num3:
        print(f"Smalles number is : {num1}")
    elif num2 <= num1 and num2 <= num3:
        print(f"Smalles number is : {num2}")
    else:
        print(f"Smallest number is : {num3}")

