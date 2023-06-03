#Print grade based on scores

n = int(input())  # Read user input as an integer and store in variable n

# Check the value of n and print the corresponding grade
if(n>=0 and n<=39):
    print("F")
elif(n>=40 and n<=50):
    print("D")
elif(n>=51 and n<=60):
    print("C")
elif(n>=61 and n<=70):
    print("B")
elif(n>=71 and n<=80):
    print("A")
elif(n>=81 and n<=100):
    print("S")
else:
    print("Invalid input")  # Print an error message if n is outside the range [0, 100]
