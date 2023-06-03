# Print 1 to n 

# Take input from the user and convert it to an integer
n = int(input())

# Iterate through the range from 1 to n+1 (exclusive)
for i in range(1, n+1):
    # Print the value of i, followed by a comma, without a newline character
    print(i, end=",")

