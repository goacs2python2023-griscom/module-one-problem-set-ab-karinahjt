#Write a function that takes a year and returns the boolean True if it is a leap year, and false if it is not.
def leapYear(year):
    if year % 4 == 0:
        if (year % 100 !=0):
            return True
        elif (year % 400 !=0):
            return False
        else:
            return True
    else:
        return False

# Test cases
print("Leap year -10: ", leapYear(-10))
print("Leap year 0: ", leapYear(0))
print("Leap year 4: ", leapYear(4))
print("Leap year 400: ", leapYear(400))
print("Leap year 444: ", leapYear(444))
print("Leap year 800: ", leapYear(800))
print("Leap year 888: ", leapYear(888))
print("Leap year 1700: ", leapYear(1700))
print("Leap year 1900: ", leapYear(1900))
print("Leap year 2000: ", leapYear(2000))
print("Leap year 2002: ", leapYear(2002))
print("Leap year 2012: ", leapYear(2012))
print("Leap year 2005: ", leapYear(2005))
print("Leap year 2023: ", leapYear(2023))