# Pentagon numbers

import math

# Define a function to check if a number is pentagonal
def pen(x):
    n = math.sqrt(24 * x + 1)
    return n % 6 == 5

# Take input for 'n' and 'k'
n = int(input())
k = int(input())

# Initialize a variable 'ans' to store the count of pairs
ans = 0

# Iterate over the range from (1+k) to 'n'
for i in range(1 + k, n):
    pi = (i * (3 * i - 1)) / 2
    pik = ((i - k) * ((3 * (i - k)) - 1)) / 2
    
    # Check if either (pi-pik) or (pi+pik) is a pentagonal number
    if pen(pi - pik) or pen(pi + pik):
        ans += 1

# Print the final count of pairs
print(ans)
