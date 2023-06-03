# Print the average of array elements

# Take input for a list of integers and store it in the variable 'a', limited to 5 elements
a = list(map(int, input().split()))[:5]

# Initialize a variable to store the sum
sum = 0

# Iterate over the elements of the list
for i in a:
    sum += i  # Add each element to the sum

# Calculate the average by dividing the sum by the number of elements (5 in this case)
avg = float(sum / 5)

# Print the average
print(avg)
