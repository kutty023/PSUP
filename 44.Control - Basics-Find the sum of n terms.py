# Find the sun of n terms

# Take input from the user and convert it to an integer
n = int(input())

# Initialize variables
sum = 0
num = 0

# Execute the following block of code while num is less than or equal to n
while(num <= n):
    # Add the value of num to the sum
    sum = sum + num
    # Increment the value of num by 1
    num = num + 1

# Print the final value of sum
print(sum)

# Take input from the user and convert it to an integer
n = int(input())

# Initialize an empty list
a = []

# Iterate through the range from 1 to n+1 (exclusive)
for i in range(1, n+1):
    # Append the value of i to the list a
    a.append(i)

# Calculate the sum of all elements in list a and print the result
print(sum(a))


