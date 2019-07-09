"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

num_args = len(sys.argv)
if num_args == 1:
    # print calendar for current month in current year (July 2019)
    current_month = datetime.now().month
    current_year = datetime.now().year    
    print(current_month, current_year)
    calendar.TextCalendar().prmonth(current_year, current_month)
    
elif num_args == 2:
    # render calendar for that month of current year
    current_year = datetime.now().year    
    month = int(sys.argv[1])
    print(month, current_year)
    calendar.TextCalendar().prmonth(current_year, month)

elif num_args == 3:
    # render calendar for that month and year
    month = int(sys.argv[1])
    year = int(sys.argv[2])
    print(month, year)
    calendar.TextCalendar().prmonth(year, month)
else:
    print("Expected format: 14_cal.py month year ")


# EXTRA NOTES
"""
from datetime import datetime

currentSecond= datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year

Entire Year:
calendar.TextCalendar().pryear(2019)

Specific month from specific year:
calendar.TextCalendar().prmonth(year, month)


"""