# Swap the largest and smallest element from the array

# Take input for the length of the array
n = int(input())

# Take input for the array elements and split them
arr = list(map(int, input().split()))[:n]

# Sort the array in ascending order
arr.sort()

# Swap the first and last elements of the sorted array
temp = arr[0]
arr[0] = arr[-1]
arr[-1] = temp

# Print the modified array elements separated by a space
print(*arr)



# Swap elements using tuple unpacking
arr[0], arr[-1] = arr[-1], arr[0]

print(*arr)