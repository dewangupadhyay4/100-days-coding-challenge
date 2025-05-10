name=str(input("Enter the name"))
age=int(input("Enter the age"))
salary=float(input("Enter the salary"))
states_visit=['Uttar Praesh', 'Maharashtra','Gujrat']
interest=('Python','Java','MySQL')
personal_things={'mobile','laptop','earbud','watch','mobile'}
water_intake={'Day1':4,'Day2':3,'Day3':3}

print(f"Hello {name}, your age is {age} and you earn Rs. {salary}")
print(f"you have visited in states like {states_visit}, \n interest in {interest}, \n personal things what you have {personal_things}, \n and your water intake in a day is {water_intake}")

print(type(name))
print(type(age))
print(type(salary))
print(type(states_visit))
print(type(interest))
print(type(personal_things))
print(type(water_intake))
