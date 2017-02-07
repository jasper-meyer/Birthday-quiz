"""
birthday.py
Author: Jasper Meyer
Credit: will, brendan
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

name = input("Hello, what is your name? ")
month = input("Hi {0}, what was the name of the month you were born in? " .format(name))
year = input("And what year were you born in, {0}? " .format(name))
day = input("And the day? ")
month = month.lower()



if month == "december" or month == "january" or month == "february":
    season = "winter"
elif month == "march" or month == "april" or month == "may":
    season = "spring"
elif month == "june" or month == "july" or month == "august":
    season = "summer"
elif month == "september" or month == "october" or month == "november":
    season = "fall"
    
if int(year) < 1980:
    era = "Stone Age"
elif int(year) >= 1980 and int(year) <= 1989:
    era = "eighties"
elif int(year) >= 1990 and int(year) <= 1999:
    era = "nineties"
elif int(year) >= 2000:
    era = "two thousands"

if todaymonth ==1:
    todaymonthh="january"
elif todaymonth ==2:
    todaymonthh="february"
elif todaymonth ==3:
    todaymonthh="march"
elif todaymonth ==4:
    todaymonthh="april"
elif todaymonth ==5:
    todaymonthh="may"
elif todaymonth ==6:
    todaymonthh="june"
elif todaymonth ==7:
    todaymonthh="july"
elif todaymonth ==8:
    todaymonthh="august"
elif todaymonth ==9:
    todaymonthh="september"
elif todaymonth ==10:
    todaymonthh="october"
elif todaymonth ==11:
    todaymonthh="november"
elif todaymonth ==12:
    todaymonthh="december"
    
    
if month == "october" and int(day) == 31:
    print ("You were born on Halloween! ")
elif todaydate == int(day) and todaymonthh == month:
    print ("Happy birthday! ")
else: 
    print ("{0}, you are a {1} baby of the {2}. " .format(name,season,era))
    






