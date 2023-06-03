# Print sum of elements present at even index

# Take input for the integer n
n = int(input())

# Take input for the list of integers a
a = list(map(int, input().split()))

sum = 0  # Initialize the sum variable to 0

# Iterate over the indices of the list 'a' with a step size of 2
for i in range(0, n, 2):
    sum += a[i]  # Add the element at the current even index to the sum

print(sum)  # Print the sum
