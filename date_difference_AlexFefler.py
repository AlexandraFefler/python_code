import datetime
import random
import math


today = datetime.datetime.now()
thisYear = int(today.year)
thisMonth = int(today.month)
year = int(random.randint(1980, thisYear))
month = int(random.randint(1, 12))
diff = 0  # difference only in months
if (thisYear == year):
    diff = math.fabs(thisMonth - month)
else:  # thisYear == year, which can be only thisYear > year
    diff = (thisYear - year - 1) * 12 + thisMonth + (12 - month)
print(str(diff % 12) + "/" + str(int(diff / 12)))
