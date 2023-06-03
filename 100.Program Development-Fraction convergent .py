# Fraction convergent

n, m = map(int, input().split())

def fraction(a, b):
    gcd = 1  # Initialize the greatest common divisor

    # Find the greatest common divisor using Euclid's algorithm
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return a // gcd, b // gcd  # Return the simplified fraction

print(*fraction(n, m))  # Print the simplified fraction
