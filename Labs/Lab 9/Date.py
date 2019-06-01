'''
Start to the Date class for Lab 9.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','September', 'October', 'November', 'December' ]

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        
    def __str__(self):
        return str(self.year)+'/'+str(self.month)+'/'+str(self.day)
    
    def __lt__(self, test):
        if self.year == test.year and self.month == test.month and self.day < test.day:
            return True
        elif self.year == test.year and self.month < test.month:
            return True
        elif self.year < test.year:
            return True
        return False
    
    def same_day_in_year(self, test):
        return self.month == test.month and self.day == test.day
    
    def is_leap_year(self):
        i = False
        if self.year % 4 == 0 and not self.year % 100 == 0:
            i = True
        if self.year % 400 == 0:
            i = True
        return i


if __name__ == "__main__":
    d1 = Date(1972, 3, 27)
    d2 = Date(1900, 4, 13)
    d3 = Date(1996, 4, 13)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print (d1.is_leap_year())
    print (d2.is_leap_year())
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1998, 5, 13)
    d4 = Date(1998, 4, 11)    
    print(d1 < d2)
    print(d2 < d3)
    print(d3 < d4)
