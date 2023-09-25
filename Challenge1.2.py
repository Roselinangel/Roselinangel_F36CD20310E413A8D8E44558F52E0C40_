def isLeapYear(Year):
 if(Year % 4 == 0 and year % 100!=0)or year % 400 == 0:
  return True
 else:
  return False


year = int(input("Enter a year:"))
if isLeapYear(year):
 Print("{}is a leap year.".format(year))
else:
 print("{}isnotaleapyear.".format(year))