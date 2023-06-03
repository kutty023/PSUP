# Divisible by 7

# Take input for the string
n = input()

# Define a function to check if there is any number divisible by 7 in the string
def toCheck(d):
    ans = 0
    for i in d:
        # Convert the current digit to an integer and update the 'ans' variable
        ans = ans * 10 + int(i)
        # Check if 'ans' is divisible by 7
        if ans % 7 == 0:
            # If so, return 1 indicating a number divisible by 7 exists
            return 1
    # If no number divisible by 7 is found, return 0
    return 0

# Call the toCheck function with the input string and print the result
print(toCheck(n))
