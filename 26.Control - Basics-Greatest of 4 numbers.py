# Printing the greates of 4 numbers

# Read the numbers from the user and store it in the variables n1,n2,n3,n4
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

# Compare the four numbers and print the greatest one
if(n1>=n2 and n1>=n3 and n1>=n4):
        print(n1)
elif(n2>=n1 and n2>=n3 and n2>=n4):
        print(n2)
elif(n3>=n1 and n3>=n2 and n3>=n4):
        print(n3)
elif(n4>=n1 and n4>=n2 and n4>=n3):
        print(n4)
else:
        print("Invalid")   # Print "Invalid" if none of the numbers is the greatest
