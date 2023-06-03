# Find whether a given year is leap year or not

year = int(input())  # Read an integer input from the user and store it in year

if (year % 4 == 0) and (year % 100 != 0):  # Check if the year is divisible by 4 but not divisible by 100
    print("leap year")  # If it is, print "leap year" to indicate that the year is a leap year
elif (year % 400 == 0) and (year % 100 == 0):  # Check if the year is divisible by 400 and also divisible by 100
    print("leap year")  # If it is, print "leap year" to indicate that the year is a leap year
else:
    print("not leap year")  # If neither of the conditions is true, print "not leap year" to indicate that the year is not a leap year
