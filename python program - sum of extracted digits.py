# Please write a program to extract the second last digit of those 2 numbers and print the sum of extracted digits.

#Getting user inputs
n1 = int(input())
n2 = int(input())
if (n1<10 or n2<10):  # Checking if the input has more than a single digit
    print("Invalid number") 
else:  
    # Eliminating the last digit
    digit1 = n1/10
    digit2 = n2/10
    # geting the last digit i.e, the second last digit of and adding them
    sum = (digit1%10) + (digit2%10)
    # printing the sum in integer form
    print(int(sum))