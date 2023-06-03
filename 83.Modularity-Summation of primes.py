# Summation of primes

# Take the input value of 'n'
n = int(input())

# Initialize a variable 's' to store the sum of prime numbers
s = 0

# Define a function to check if a number is prime
def isPrime(N):
    # Check if N is equal to 0 or 1, which are not prime numbers
    if N == 1 or N == 0:
        return False
    # Iterate from 2 to N-1 to check for divisibility
    for i in range(2, N):
        if N % i == 0:
            return False
    # If no divisor is found, N is a prime number
    return True

# Iterate from 2 to n (inclusive)
for i in range(2, n + 1):
    # Check if the current number 'i' is prime
    if isPrime(i):
        # If 'i' is prime, add it to the sum 's'
        s += i

# Print the sum of prime numbers up to 'n'
print(s)
