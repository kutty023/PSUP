# Print the largest and smallest number of Input numbers

# Take input from the user and convert it to an integer
n = int(input())

# Initialize an empty list
k = []

# Iterate through the range from 1 to n+1 (exclusive)
for i in range(1, n+1):
    # Take input from the user and convert it to an integer
    num = int(input())
    # Append the value of num to the list k
    k.append(num)

# Print the largest value in the list k using the max() function
print("largest =", max(k))

# Print the smallest value in the list k using the min() function
print("smallest =", min(k))

