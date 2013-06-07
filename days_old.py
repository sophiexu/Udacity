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

def countWholeYears(year1, year2, month1, month2, day1, day2):
    if year2 == year1: # you are less than a year old
        return 0 # you are zero years old
    if year2 - year1 == 1 and month1 > month2: # you are less than a year old
        return 0 # you are zero years old
    if year2 - year1 == 1 and month1 == month2: # you are within a month of one year old
        if day1 > day2: # you are zero years old
            return 0
        elif day2 <= day1: # you are just barely over one year old!  Let's see if it was a leap year!
            # which february were you alive for?
            if month1 <= 2: # you were born before the february of your birth-year
                if isLeapYear(year1):
                    return 366
            else: # february didn't happen till the following year
                if isLeapYear(year2):
                    return 366 
            return 365 # your first year on this earth was not a leap year!
    if year2 - year1 == 1 and month1 < month2: #you are over a year old
            # which february were you alive for?
            if month1 <= 2: # you were born before the february of your birth-year
                if isLeapYear(year1):
                    return 366
            elif month2 > 2: # february didn't happen till the following year
                if isLeapYear(year2):
                    return 366 
            return 365 # your first year on this earth was not a leap year!

    year_counter = year1 + 1 # to get first count, only use whole years
    # first, count whole years, accounting for leap years
    day_total = 0    
    while year_counter < year2:
        day_total = day_total + 365
        if isLeapYear(year_counter): # if leap year, add extra day
            day_total = day_total + 1          
        year_counter = year_counter + 1 
    return day_total

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    num_days_in_year = 365
    num_days_in_leap_year = 366
    num_days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

   
    day_total = countWholeYears(year1, year2, month1, month2, day1, day2)
    print "initial day total is:"
    print day_total

    if year1 == year2: 
        # print "got here1"
        if month1 == month2: # still in same month you were borh
            day_total = day_total + num_days_in_months[month1 - 1] - day1 - day2
        else: # not in same month you were born
            day_total = day_total + num_days_in_months[month1 - 1] - day1
            # Count whole days that are left over from year2
            day_total = day_total + day2 # can take number of days at face value
            # now count intermediary months
            if month2 > month1:
                month_counter = month1 + 1  # e.g. if you were born in march, month_counter = 3+1 = 4
        
                # count remaining number of days in whole months of your birth year
                while month_counter < month2: # if month2 = march, 3
                    day_total = day_total + num_days_in_months[month_counter - 1]
                    month_counter = month_counter + 1
                # was february in that month?  Is it in a leap-year?
                if isLeapYear(year1) and month1 <= 2 and month2 > 2:
                    day_total = day_total + 1

    elif year2 - year1 == 1:
        # print "got here2"
        if month1 > month2: # been alive less than one year
            print "got here 1"
            month_counter = month1 + 1  # e.g. if you were born in march, month_counter = 3+1 = 4        
            # count remaining number of days in whole months of your birth year
            while month_counter < 12: # count from start month to december
                day_total = day_total + num_days_in_months[month_counter - 1]
                month_counter = month_counter + 1
                # was february in that month?  Is it in a leap-year?
            if isLeapYear(year1) and month1 <= 2:
                day_total = day_total + 1
            # count from december to month 2
            month_counter = 0
            while month_counter < month2: # count from start month to december
                day_total = day_total + num_days_in_months[month_counter - 1]
                month_counter = month_counter + 1
                # was february in that month?  Is it in a leap-year?
            if isLeapYear(year2) and month2 >= 2:
                day_total = day_total + 1

        elif month1 == month2: # been alive approximately one year
            day_total = day_total + day2 - day1
        elif month1 < month2: # been alive over one year
            print "got here 3"
    
    else: # alive for more than one ful year and day_total should already be > 0
        print "got here3"
        # next, count whole months remaining from year1    
        month_counter = month1 + 1  # e.g. if you were born in march, month_counter = 3+1 = 4
        
        # count remaining number of days in your birth year based on months
        while month_counter <= 12: 
            day_total = day_total + num_days_in_months[month_counter - 1]
            month_counter = month_counter + 1

        # did your birth year include a leap day that you were alive for?!
        if month1 <= 2: # you were born before the february of your birth-year
            if isLeapYear(year1):
                day_total = day_total + 1

        # count the remaining months from year2
        month_counter = 0
        while month_counter < month2-2:
            day_total = day_total + num_days_in_months[month_counter]
            month_counter = month_counter + 1


        day_total = day_total + day2 # can take number of days at face value


    print day_total
    return day_total

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
