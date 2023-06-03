# Largest product in a series

# Take input for the value of k
k = int(input())

# Take input for the number as a string
numbers = input()

# Initialize the variable to store the largest product
largest = 0

# Iterate over each possible contiguous segment of length k in the number
for i in range(len(numbers) - k + 1):
    # Initialize the product variable for the current segment
    product = 1
    
    # Calculate the product of the current segment
    for j in range(i, i + k):
        product *= int(numbers[j])
    
    # Compare the product with the largest product found so far
    if product > largest:
        largest = product
        print(largest)
