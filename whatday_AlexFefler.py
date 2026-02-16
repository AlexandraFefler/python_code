import datetime
import time
from enum import Enum


class Week(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


# Initialize the date parameters
day = datetime.datetime.now().day
month = 8
year = int(input("Enter a year: "))
date = datetime.datetime(year, month, day)

print("Processing.", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".", end="")

# Get the day name from the Week enum
weekday = date.isoweekday()
weekday = Week(weekday) # not Week[weekday]
strr = str(weekday).removeprefix("Week.") # remove part of the string so the result in consule will look neat (according to mission)
strrr = str(date).removesuffix(" 00:00:00") # remove part of the string so the result in consule will look neat (according to mission)
print(strrr, "was a", strr)