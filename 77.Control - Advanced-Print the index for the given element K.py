# Print the index for the given element K

# Take input for the integer n
n = int(input())

# Take input for the list of integers a, and only consider the first 'n' elements
a = list(map(int, input().split()))[:n]

# Take input for the integer k
k = int(input())

# Initialize the index to -1, indicating that the element is not found initially
index = -1

# Iterate over each element in the list 'a'
for i in range(0, len(a)):
    if a[i] == k:  # Check if the current element matches the value of 'k'
        index = i  # Update the index variable with the current index
        break  # Exit the loop since the element is found

# Print the value of 'index', which represents the index of the element 'k' in the list 'a'
print(index)
