# Greater among extracted digits post decimal point using python 

n1 = float(input())  # Read the first float input from the user and store it in n1
n2 = float(input())  # Read the second float input from the user and store it in n2

c = (int((n1*10)%10))  # Multiply n1 by 10, take the modulo 10, and convert it to an integer. Store the result in c
d = (int((n2*10)%10))  # Multiply n2 by 10, take the modulo 10, and convert it to an integer. Store the result in d

if c > d:  # Check if c is greater than d
    print(c)  # If it is, print the value of c
elif c == d:  # If c is not greater than d, check if c is equal to d
    print("The digits are equal")  # If they are equal, print the message "The digits are equal"
else:
    print(d)  # If c is not greater than d and c is not equal to d, print the value of d
