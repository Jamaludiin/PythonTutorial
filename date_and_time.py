# lets use the module called datetime to deal with dates. to use it we must import it

import datetime

# lets read the current date and time
current_date_time = datetime.datetime.now()
print(current_date_time)


# lets be specific and use its methods
print("The current year is", current_date_time.year)
print("The current month is", current_date_time.month)
print("The current day is", current_date_time.day)
#print("The current day is", current_date_time.time)

print("\n")
# format the date object into readable string
print(current_date_time.strftime("%A")) # Weekday, full version	Wednesday
print(current_date_time.strftime("%a")) # Weekday, short version	Wed

print("\n")
print(current_date_time.strftime("%B")) # Month name, full version	December
print(current_date_time.strftime("%b")) # Month name, short version	Dec

print("\n")
print(current_date_time.strftime("%W")) # Weekday as a number 0-6, 0 is Sunday	3
print(current_date_time.strftime("%d")) # Day of month 01-31	31

print("\n")
print(current_date_time.strftime("%Y")) # Year, full version	2023
print(current_date_time.strftime("%y")) # Year, short version, without century	23

print("\n")
print(current_date_time.strftime("%C")) # entury	20
print(current_date_time.strftime("%c")) # Local version of date and time	Mon Dec 31 17:41:00 2018

print("\n")
print(current_date_time.strftime("%G")) # ISO 8601 year	2018
print(current_date_time.strftime("%j")) # Day number of year 001-366	365