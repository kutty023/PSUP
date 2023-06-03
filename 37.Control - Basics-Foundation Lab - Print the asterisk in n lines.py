# Print the *(asterisk) in n lines/

n = int(input())  # Read an integer input from the user and store it in n

for i in range(1, n+1):  # Iterate over numbers from 1 to n (inclusive)
    print('*' * n)  # Print a line of n asterisks ('*') using string repetition
