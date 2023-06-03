# Print the smallest element of the array

# Take input for a list of integers and store it in the variable 'a', limited to 8 elements
a = list(map(int, input().split()))[:8]

# Assign the first element of the list to the variable 'l' as the initial minimum
smallest = a[0]

# Iterate over the elements of the list
for i in a:
    # Check if the current element 'i' is less than or equal to the current minimum 'l'
    if i <= smallest:
        smallest = i  # Update the minimum to the new value

# Print the minimum element
print(smallest)
