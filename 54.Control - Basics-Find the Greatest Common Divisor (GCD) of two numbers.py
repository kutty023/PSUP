# Find the Greatest Common Divisor (GCD) of two numbers

n1, n2 = [int(x) for x in input().split()]
# Takes two integers as input from the user

for i in range(1, min(n1, n2) + 1):
    # Iterates through the numbers from 1 to the minimum of n1 and n2

    if n1 % i == 0 and n2 % i == 0:
        # Checks if both n1 and n2 are divisible by i without leaving any remainder

        gcd = i
        # Updates the variable gcd with the current value of i (if it is a common factor)

print(gcd)
# Prints the greatest common divisor (gcd) of n1 and n2
