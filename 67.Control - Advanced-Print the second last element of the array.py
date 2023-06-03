# Print the second last element of the array

# Take input for the value of n
n = int(input())

# Take input for a list of integers and store it in the variable 'arr', limited to 'n' elements
arr = list(map(int, input().split()))[:n]

# Print the second-to-last element of the list 'arr'
print(arr[-2])
