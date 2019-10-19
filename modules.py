#DATE TIME MODULE
# How to perform Calculations using DATE TIME Module
import datetime as dt
dob = "1998-14-11"
today = "27/7/2019"

dtime = dt.datetime.strptime(dob,"%Y-%d-%m") # Converting Your DOB into Datetime
print(dtime)

d2time = dt.datetime.strptime(today,"%d/%m/%Y") # Converting Today's date into Datetime
print(d2time)

todaydt = d2time - dtime
print(todaydt)

year_old= d2time.year - dtime.year

print(dtime.strftime("%A %d" " " "%B"))
print(year_old)

#How to Add days in a datetime
# for example what will be the date after 4 weeks
dob4weeks = dt.timedelta(days=28)
new_date = d2time + dob4weeks
print("Your test is scheduled on "+ (new_date.strftime("%A" " " "%d" " " "%B""-""%Y")))

# MATH Module
import math
print(math.ceil(2.7))
print(math.floor(2.8))
print(math.factorial(5))
print(math.fmod(9,3))
print(math.fabs(-2.7))

#RANDOM Module
import random

print(random.randint(1,100))

print(random.choice([1,2,3,6,]))

#OS MODULE
import os
#print(os.listdir('.'))
