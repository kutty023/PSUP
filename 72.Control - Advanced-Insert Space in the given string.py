# Insert Space in the given string

# Take input for the string
a = input()

# Initialize an empty string to store the modified string
l = ''

# Iterate over the range of indices in the string (except the last index)
for i in range(len(a)-1):
    # Check if the current character is lowercase and the next character is uppercase
    if a[i].islower() and a[i+1].isupper():
        l = l + a[i]  # Add the lowercase character to the modified string
        l = l + " "   # Add a space between the lowercase and uppercase characters
    else:
        l += a[i]  # Add the character to the modified string as it is

# Add the last character to the modified string
l += a[-1]

# Print the modified string
print(l)
