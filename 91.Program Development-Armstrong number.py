# Armstrong number

n = int(input())  # Take an integer input

# Calculate the length of the number n
p = len(str(n))

s = 0  # Initialize sum variable to 0
t = n  # Assign the value of n to a temporary variable t

# Calculate the sum of digits raised to the power p
while t > 0:
    d = t % 10  # Get the last digit of t
    s += d ** p  # Add the digit raised to the power p to the sum
    t //= 10  # Remove the last digit from t by integer division

# Check if n is equal to the sum of digits raised to the power p
if n == s:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
