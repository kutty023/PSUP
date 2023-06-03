# Sort the array in ascending order

# Take input for the length of the array
n = int(input())

# Take input for the array elements, limit to n elements
a = list(map(int, input().split()))[:n]

# Sort the array in ascending order
a.sort()

# Print the sorted array elements separated by a space
print(*a)
