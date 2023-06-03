# Pandigital number

w = int(input())  # Take an integer input

def pandigit(e):
    n = str(e)  # Convert the input integer to a string
    if len(n) != 5:
        return "No"  # If the string length is not equal to 5, it's not a pandigital number

    d = set(n)  # Create a set of unique characters in the string
    if len(d) == 5 and '0' not in d:
        return "Yes"  # If there are exactly 5 unique non-zero digits, it's a pandigital number
    else:
        return "No"  # Otherwise, it's not a pandigital number

print(pandigit(w))  # Print the result of the pandigit function
