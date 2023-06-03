# Print the even elements in an array

# Take input for a list of integers and store it in the variable 'a'
a = list(map(int, input().split()))[:10]

# Iterate over the elements of the list
for i in range(0, len(a)):
    # Check if the element is non-zero and even
    if a[i] != 0 and a[i] % 2 == 0:
        # Print the element
        print(a[i], end=" ")
        
