# Print the greatest of two numbers

n1 = int(input())  # Read an integer input from the user and store it in n1
n2 = int(input())  # Read another integer input from the user and store it in n2

if n1 > n2:  # Check if n1 is greater than n2
    print(n1)  # If it is, print the value of n1
elif n1 == n2:  # If n1 is not greater than n2, check if n1 is equal to n2
    print(n1)  # If they are equal, print the value of n1
else:
    print(n2)  # If n1 is not greater than n2 and n1 is not equal to n2, print the value of n2
