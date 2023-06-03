# Powerful Digit Counts

n = int(input())

# Iterate over values of n from 1 to 10
for i in range(1, 11):
    # Calculate the nth power of i
    r = str(pow(i, n))

    # Check if the number has n digits
    if len(r) == n:
        print(r)  # Print the smallest n-digit positive integer
        break
