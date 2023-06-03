# Remove the special characters in the given string

# Take input for the string
a = input()

# Initialize an empty string to store the alphabetic characters
alpha = ''

# Iterate over each character in the string
for i in a:
    # Check if the character is alphabetic
    if i.isalpha():
        alpha += i  # Append the alphabetic character to the 'alpha' string

# Print the 'alpha' string containing only the alphabetic characters
print(alpha)
