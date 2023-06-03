# Move all Hashes

w = input()  # Take a string input

h, v = '', ''  # Initialize empty strings for '#' and non-'#' characters

for i in w:
    if i == '#':
        h += i  # Append '#' to the 'h' string
    else:
        v += i  # Append non-'#' character to the 'v' string

print(h + v)  # Print the concatenation of 'h' and 'v' strings
