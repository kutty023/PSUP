# Print the elements of array

# Take input for the integer n
n = int(input())

arr = []  # Initialize an empty list

# Continue taking input until the length of the list is less than 'n'
while len(arr) < n:
    a = int(input())  # Prompt the user to enter an integer
    arr.append(a)  # Add the integer to the list 'arr'

# Print the elements of the list separated by commas and with a trailing comma
print(*arr, sep=',', end=",")

        