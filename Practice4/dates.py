import datetime #Return the year and name of weekday:

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

import datetime #now time

x = datetime.datetime.now()

print(x) 

import datetime #Create a date object:

x = datetime.datetime(2020, 5, 17)

print(x)

#Display the name of the month:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

