# Kth Prime number

# Assign the value 104 to the variable n
n = 104

# Take input for k, representing the k-th prime number
k = int(input())

# Create an empty list l to store the prime numbers
l = []

# Define a function to check if a number N is prime
def isPrime(N):
    if N == 1 or N == 0:
        return False
    for i in range(2, N):
        if N % i == 0:
            return False
    return True

# Iterate from 2 to n (inclusive)
for i in range(2, n + 1):
    # Check if i is a prime number
    if isPrime(i):
        # If i is prime, append it to the list l
        l.append(i)

# Print the k-th prime number from the list l
print(l[k - 1])
