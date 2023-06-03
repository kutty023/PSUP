# Largest Digit

# Take input for the values of s and d
s, d = map(int, input().split())

# Check the conditions for forming the desired sequence
if s <= 9 * d and s > 0 and d > 0 and d < 5 and s <= 36:
    ans = ''  # Initialize an empty string to store the sequence
    for i in range(d):
        if s >= 9:
            ans += str(9)  # Append '9' to the sequence
            s = s - 9  # Subtract 9 from the sum
        else:
            ans += str(s)  # Append the remaining sum to the sequence
            s = 0  # Set the sum to 0 as it has been fully used
    print(ans)  # Print the resulting sequence
else:
    print(-1)  # If the conditions are not met, print -1
