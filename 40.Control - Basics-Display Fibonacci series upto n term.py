# Display Fibonacci series upto n term

num = int(input())  # Read an integer input from the user and store it in the variable num
idn = 0  # Initialize the variable idn to 0
n1 = 0  # Initialize the variable n1 to 0
n2 = 1  # Initialize the variable n2 to 1

if num <= 0:  # Check if num is less than or equal to 0
    print("Invalid")  # If num is less than or equal to 0, print "Invalid"
elif num == 1:  # Check if num is equal to 1
    print(n1)  # If num is equal to 1, print the value of n1
else:
    while idn <= num:  # Iterate while idn is less than or equal to num
        print(n1, end=" ")  # Print the value of n1 followed by a space without a newline
        fab = n1 + n2  # Calculate the next Fibonacci number by adding n1 and n2
        n1 = n2  # Update the value of n1 to be the same as n2
        n2 = fab  # Update the value of n2 to be the calculated Fibonacci number
        idn += 1  # Increment idn by 1