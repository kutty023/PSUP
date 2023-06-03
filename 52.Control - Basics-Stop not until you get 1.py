# Stop not until you get 1

# Initialize an empty list
v = []

# Continue taking input from the user until the loop is explicitly broken
while True:
    # Take input from the user and convert it to an integer
    num = int(input())
    # Append the value of num to the list v
    v.append(num)
    # Check if the entered number is equal to 1
    if num == 1:
        # Break out of the loop if the condition is true
        break

# Print the largest value in the list v using the max() function
# and the smallest value using the min() function
print(max(v), min(v))

