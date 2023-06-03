# Python program to extract 2nd last digit :

n = int(input())  # Read user input and store as an integer in variable n

# Check if n is greater than or equal to 10
if(n>=10):          
    s = int(n/10)%10   # If n is greater than or equal to 10, divide it by 10, convert the result to an integer, and take the ones digit (i.e., the second-to-last digit)
    print(s)  # Print the second-to-last digit of n
else:
    print("Invalid number")  # If n is less than 10, print "Invalid number"



# the above code works only for positive numbers, for both positive and negative numbers is:

n = int(input())  # Read user input and store as an integer in variable n

# Check if the absolute value of n is less than 10, and print an error message if true
if(abs(n)<10):
    print("Invalid input")
else:  # If the absolute value of n is 10 or greater, continue with the following code
    s = (int(abs(n)/10)%10)  # Divide the absolute value of n by 10, convert the result to an integer, and take the ones digit (i.e., the second-to-last digit)
    print(s)  # Print the second-to-last digit of n (or -n if n is negative)

