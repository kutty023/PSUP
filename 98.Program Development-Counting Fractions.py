# Counting Fractions

a, b = map(int, input().split())

def fraction(m, n):
    gcd = 1  # Initialize the greatest common divisor
    common_divisors = 0  # Initialize the count of common divisors

    # Find the greatest common divisor using Euclid's algorithm
    for i in range(1, min(m, n) + 1):
        if m % i == 0 and n % i == 0:
            gcd = i
            common_divisors += 1

    return common_divisors

print(fraction(a, b))
