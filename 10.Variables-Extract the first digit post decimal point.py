# Extract the first digit post decimal point

n = float(input())  # Read user input as a floating-point number and store in variable n

# Compute the first digit after the decimal point of the absolute value of n
s = int(abs(n)*10)%10

print(s)  # Print the first digit after the decimal point of n (or -n if n is negative)
