# Sum square difference

# Take input for the value of n
n = int(input())

# Initialize variables for sum of squares (s), sum of numbers (sq), and square of the sum (ssq)
s ,sq, ssq = 0, 0, 0

# Iterate from 1 to n (inclusive)
for i in range(1, n + 1):
    # Add the square of the current number to the sum of squares
    s += i ** 2
    # Add the current number to the sum of numbers
    sq += i

# Calculate the square of the sum
ssq = sq ** 2

# Print the absolute difference between the square of the sum and the sum of squares
print(abs(ssq - s))
