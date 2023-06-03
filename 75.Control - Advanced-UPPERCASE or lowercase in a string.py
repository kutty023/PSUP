# UPPERCASE or lowercase in a string

# Take input for the string
a = input()

# Remove any spaces from the input string using the replace() method
w = a.replace(' ', '')

# Initialize counters for lowercase and uppercase letters
l, u = 0, 0

# Iterate over each character in the modified string 'w'
for i in w:
    if i.isupper():  # Check if the character is uppercase
        u += 1  # Increment the uppercase counter
    if i.islower():  # Check if the character is lowercase
        l += 1  # Increment the lowercase counter

# Compare the lengths of the modified string with the lowercase and uppercase counters
if len(w) == l:
    print('L')  # If the lengths match, it means the string contains only lowercase letters
elif len(w) == u:
    print('U')  # If the lengths match, it means the string contains only uppercase letters
else:
    print('Both')  # If neither condition is met, it means the string contains both lowercase and uppercase letters
