# Project Euler: Problem 19
# Jonathan Kosasih

#You are given the following information, but you may prefer to do some research for yourself.
#
#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#------------------------------------------------------------------
import datetime
# easy way, just use python datetime and check if the first day of the month is a sunday
def answer():
    ans = sum( 1
        for year in range(1901, 2001)
        for month in range(1, 13)
        if datetime.date(year, month, 1).weekday() == 6)
    return ans

# if no import datetime
def answerNoImport():
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Jan 1 1901 was a Tuesday, day = 2
    day = 2
    sundays = 0
    for year in range(1901,2001):
        for m in months:
            day += m
            if(year % 4 == 0 and m == 28):
                day += 1
            if(day % 7 == 0):
                sundays += 1
    return sundays
    

print(str(answer()))
print(str(answerNoImport()))
print("Test complete")