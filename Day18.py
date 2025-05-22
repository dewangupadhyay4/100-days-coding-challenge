import datetime
from datetime import timedelta

# now = datetime.datetime.now()
# print("current date and time is ", now)
# print("current date  is ", now.date())
# print("current time is ", now.time())

# print("")

# birthdate=datetime.date(2003,10,22)
# print(birthdate)

# today=datetime.datetime.today()
# print("Today: ",today)

# future=today+timedelta(days=12)
# print("12 days later: ",future)

# past=today-timedelta(days=12)
# print("Before 12 days: ",past)

birthdate=input("Enter your birthdate: ")
birth_date=datetime.datetime.strptime(birthdate,"%d-%m-%Y")

today=datetime.datetime.today()
this_year_birthday=birth_date.replace(year=today.year)

if this_year_birthday < today:
    this_year_birthday=this_year_birthday.replace(year=today.year+1)

days_left=this_year_birthday - today
print(days_left)