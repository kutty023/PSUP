#  Find whether given year is even or odd

n = int(input())  # Read an integer input from the user and store it in n

if n % 2 == 0:  # Check if the remainder of n divided by 2 is equal to 0
    print("Even")  # If it is, print "Even" to indicate that the number is even
else:
    print("Odd")  # If the remainder of n divided by 2 is not 0, print "Odd" to indicate that the number is odd
