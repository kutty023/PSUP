# Python program to extract 2nd last digit

n = int(input()) #Getting input from the user
if(n>=10):          #checking if the input contains more than one digit
    s = int(n/10)%10    #n is divided by 10 to remove the last digit and then gets the remainder using modulus
    print(s)
else:
    print("Invalid number") #if n is lessthan 10 prints invalid