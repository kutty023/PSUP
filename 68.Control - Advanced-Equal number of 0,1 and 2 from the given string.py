# Equal number of 0,1 and 2 from the given string

# Take input for the string
a = input()

# Initialize variables to store the counts
z, o, t = 0, 0, 0

# Iterate over each character in the string
for i in a:
    if i == '0':
        z += 1  # Increment the count of '0'
    elif i == '1':
        o += 1  # Increment the count of '1'
    elif i == '2':
        t += 1  # Increment the count of '2'

# Check if the counts of '0', '1', and '2' are equal
if z == o and o == t:
    print("Yes")
else:
    print("No")
