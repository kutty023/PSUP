# Calculate the cube of all numbers from 1 to n 

# Take input from the user and convert it to an integer
n = int(input())

# Initialize the variable i to 1
i = 1

# Execute the following block of code while i is less than or equal to n
while(i <= n):
    # Print the cube of i with a space after each number
    print(i**3, end=' ')
    # Increment the value of i by 1
    i += 1
