# Check if string is rotated by two place

# Take two input strings 'a' and 'b'
a, b = input().split()

# Define a function to check for rotational relationship
def rotateA(av, bv):
    # Check if the last two characters of 'a' match the first two characters of 'b'
    if av[0:2] == bv[-2:]:
        return 1
    # Check if the first two characters of 'a' match the last two characters of 'b'
    if av[-2:] == bv[0:2]:
        return 1
    # Return 0 if no rotational relationship is found
    else:
        return 0

# Print the result of the rotational relationship check
print(rotateA(a, b))
