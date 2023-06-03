# Print the multiplication table for x

# Take input from the user and convert it to an integer
x = int(input())

# Iterate through the range from 1 to 11 (exclusive)
for i in range(1, 11):
    # Print the multiplication table: x, multiplier, "=", and the result without any separators
    print(x, "x", i, "=", x * i, sep='')

