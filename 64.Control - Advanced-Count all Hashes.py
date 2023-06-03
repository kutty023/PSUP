# Count all Hashes

# Take input for the word
word = input()

# Define the function countHash that counts the number of '#' characters in a given string
def countHash(l):
    a = 0  # Initialize a variable to store the count
    for i in range(0, len(l)):
        if l[i] == "#":
            a += 1  # Increment the count by 1 for each '#' character encountered
    return str(a)  # Convert the count to a string and return it

# Call the countHash function with the input word and print the resulting count
print(countHash(word))
