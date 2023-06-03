# Sum of digits in a string

# Take input for the string
string = input()

# Define a function to calculate the sum of numeric digits in a string
def numberSum(s):
    sum = 0
    for i in s:
        # Check if the character is numeric
        if i.isnumeric():
            # If so, convert it to an integer and add it to the sum
            sum += int(i)
    return sum

# Call the numberSum function with the input string and print the result
print(numberSum(string))
