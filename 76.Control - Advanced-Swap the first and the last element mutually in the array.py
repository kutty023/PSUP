# Swap the first and the last element mutually in the array

# Take input for the integer
n = int(input())

# Take input for the list of integers, and only consider the first 'n' elements
a = list(map(int, input().split()))[:n]

# Swap the first and last elements of the list using multiple assignment
a[0], a[-1] = a[-1], a[0]

# Print the modified list using the unpacking operator *
print(*a)
