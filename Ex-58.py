"""
Exercise 58: Next Day

Write a program that reads a date (input day, month, and year separately) from the user and computes its immediate successor.
For example, if the user enters values that represent 2013-11-18 then your program should display a message indicating that the day immediately after 2013-11-18 is 2013-11-19.
If the user enters values that represent 2013-11-30 then the program should indicate that the next day is 2013-12-01.
If the user enters values that represent 2013-12-31 then the program should indicate that the next day is 2014-01-01.
The date will be entered in numeric form with three separate input statements; one for the year, one for the month, and one for the day.
Ensure that your program works correctly for leap years.
Display the date entered and next day as strings.
"""
year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))
