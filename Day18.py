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

birtday=input("Enter your Birthday: ")
converted=datetime.datetime.strptime(birtday,"%d-%m-%y")
today=datetime.datetime.today()
left=today-converted
print(left)