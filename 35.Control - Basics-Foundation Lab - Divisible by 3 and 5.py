# Divisible by 3 and 5

n = int(input())  # Read an integer input from the user and store it in n

if n % 3 == 0 and n % 5 == 0:  # Check if n is divisible by both 3 and 5
    print("Y")  # If it is, print "Y" to indicate that the number is divisible by both 3 and 5
else:
    print("N")  # If n is not divisible by both 3 and 5, print "N" to indicate that the number is not divisible by both 3 and 5
