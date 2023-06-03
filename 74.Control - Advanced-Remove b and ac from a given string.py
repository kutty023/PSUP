# Remove b and ac from a given string

# Take input for the string
a = input()

# Define a function to replace specific substrings in the string
def rep(w):
    # Replace 'b' with an empty string using the replace() method
    n = w.replace('b', '')
    
    # Replace 'ac' with an empty string using the replace() method
    c = n.replace('ac', '')
    
    # Return the modified string
    return c

# Call the rep() function with the input string 'a' and print the result
print(rep(a))


# Another solution

# Take input for the string
a = input()

# Define a function to replace specific substrings in the string
def replace(w):
    # Replace 'b' with '#' using the replace() method
    b = w.replace('b', '#')
    
    # Replace 'ac' with '#' using the replace() method
    c = b.replace('ac', '#')
    
    # Initialize an empty string to store the final result
    s = ''
    
    # Iterate over each character in the modified string 'c'
    for i in c:
        if i != '#':  # Exclude the '#' characters
            s += i  # Append the non-replaced characters to the result string
    
    # Return the final result string
    return s

# Call the replace() function with the input string 'a' and print the result
print(replace(a))
