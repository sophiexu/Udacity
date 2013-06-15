# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def isLeapYear(year):
    if year % 100 == 0:
        if year % 400 == 0 and year % 4 == 0:
            return True
        return False
    elif year % 4 == 0:
        return True
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    num_days_in_year = 365
    num_days_in_leap_year = 366
    num_days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Count the days
    years = range(year1, year2+1)
    # create variable to hold number of days of life:
    days = 0

    # Count all days of all years of your life, using whole years (rounded up)
    for year in years:
        days = days + 365
        if isLeapYear(year):
            days = days + 1

    # subtract the number of days that you shouldn't have included from the beginning of your life
    first_days = day1 # this counts the days 
    # Count days between january and your birth month, and subtract them from the total

    for month in range(month1-1):
        first_days = first_days + num_days_in_months[month]
    days = days - first_days

    # subtract the number of days you shouldn't have included from the end-date onwards
    last_days = 0

    for month in range(month2,12):
        last_days = last_days + num_days_in_months[month]
    last_days = last_days + (num_days_in_months[month2 - 1] - day2)
    days = days - last_days

    # correct for overcounted leap days!
    if isLeapYear(year1) and first_days > 2: # you should subtract a leap day because you counted one you shouldn't have
        # print 'subtracting day from day1'
        days = days - 1
    if isLeapYear(year2) and month2 < 3: # you should subtract a leap day because you counted one too many
        # print 'subtracting day from day2'
        days = days - 1
    print days
    return days

    # Test routine
#def test():
#    test_cases = [((2012,1,1,2012,2,28), 58), 
#                  ((2012,1,1,2012,3,1), 60),
#                  ((2011,6,30,2012,6,30), 366),
#                  ((2011,1,1,2012,8,8), 585 ),
#                  ((1900,1,1,1999,12,31), 36523)]
#    for (args, answer) in test_cases:
#        result = daysBetweenDates(*args)
#        if result != answer:
#            print "Test with data:", args, "failed"
#        else:
#            print "Test case passed!"
#
#test()