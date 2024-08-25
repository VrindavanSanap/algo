# Created by Vrindavan Sanap
# countins_sundays.py
#
#
#
#
#

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def leap_years_till(years):
  """
  return the number of leap years from year 0 to
  year years
  """


for i in range(0):
  print(f"i -> {leap_years_till(i)}")


def day_(day, month, year):
  """
  returns what day it was on a  given date
  valid from 1 Jan 1900 to 31 Dec 2000
  """
  if day == 1 and month == 1 and year == 1900:
    return 0
  else:
    pass


def day():
  return days[day_]


def counting_sundays():
  """
  returns the number of sundays between
  1 Jan 1901 to 31 Dec 2000
  """
  for year in range(1901, 2001):
    for month in range(1, 13):
      print(f"1 {month} {year}", end=" ")


print(leap_years(0, 4))
