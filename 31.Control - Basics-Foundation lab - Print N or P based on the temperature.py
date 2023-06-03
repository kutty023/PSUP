# Print N/P based on the temperature

n = float(input())  # Read a floating-point temperature value input from the user and store it in n

if n > 0:  # Check if n is greater than 0
    print("P")  # If it is, print "P" to indicate that the temperature is positive
else:
    print("N")  # If n is not greater than 0, print "N" to indicate that the temperature is not positive (negative or zero)
