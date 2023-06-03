# Count prime elements in an array

# Take input for a list of integers and store it in the variable 'n'
n = list(map(int, input().split()))

# Initialize a variable 'l' to store the count of prime numbers
l = 0

# Helper function to check if a number is prime
def primecount(num):
    if num <= 1:
        return 0
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return 0
    return 1

# Iterate over each element in the list 'n'
for i in n:
    # Check if the current element is a prime number by calling the 'primecount' function
    if primecount(i):
        l = l + 1  # Increment the count if the number is prime

# Print the count of prime numbers
print(l)
