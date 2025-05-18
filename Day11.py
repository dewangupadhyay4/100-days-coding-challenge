nums=[x for x in range(1,21) if x%3==0]
print(nums)

#------------------------------------------------------------------------------------------------

listing=["Python", "is", "awesome"]
length=[len(listing) for x in listing]
print(length)

#----------------------------------------------------------------------------------------------------

people = {
    "Dewang": 25,
    "Riya": 17,
    "Amit": 30,
    "Rohan": 15,
    "Sneha": 22
}

adults={name: age for name,age in people.items() if age >=18}
print(adults)