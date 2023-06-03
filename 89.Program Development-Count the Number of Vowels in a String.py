# Count the Number of Vowels in a String

s = input()  # Take input for the string

v = 'aeiou'  # Define a string of lowercase vowels
V = 'AEIOU'  # Define a string of uppercase vowels

sum = 0  # Initialize a variable 'sum' to store the count of vowels

# Iterate over each character in the string
for i in s:
    # Check if the character is a lowercase or uppercase vowel
    if i in v or i in V:
        sum += 1  # Increment the 'sum' variable by 1 if it is a vowel

print(sum)  # Print the final count of vowels
