# Print 1 to n in reverse order

# Take input from the user and convert it to an integer
n = int(input())

# Initialize an empty list
a = []

# Iterate through the range from 1 to n+1 (exclusive)
for i in range(1, n+1):
    # Append the value of i to the list a
    a.append(i)

# Reverse the order of elements in the list a
a.reverse()

# Print the elements of list a using the * operator to unpack the list
print(*a)

