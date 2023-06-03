# Print the 4th letter of the given name (using Python)

# Take input for n (as a string)
n = input()

# Check if the length of n is less than 4
if(len(n)<4):
    # If the length of n is less than 4, print an error message
    print("Try again")
else:
    # If the length of n is 4 or greater, print the 4th character of n
    print(n[3])
