# Sum of first two elements of an array

# Take input for the integer n
n = int(input())

# Take input for the list of integers a, and only consider the first 'n' elements
a = list(map(int, input().split()))[:n]

# Iterate over the first two elements in the list 'a'
for i in range(2):
    sum = 0  # Initialize the sum variable to 0 for each element

    # Iterate over the digits of the current element as a string
    for j in str(a[i]):
        sum += int(j)  # Add the digit to the sum

    # Print the sum for the current element without a new line (end="")
    print(sum, end="")
