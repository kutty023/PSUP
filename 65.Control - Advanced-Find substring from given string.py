# Find substring from given string

# Take input for the word
w = input()

# Take input for the index and length of substrings
i, l = map(int, input().split())

# Define the function substring that generates all possible substrings of a given word
def substring(word, index, length):
    sub = set()  # Initialize a set to store unique substrings
    for i in range(0, len(word)):
        value = ''
        i = index  # Assign the specified index to i
        for j in range(i, len(word)):
            value += word[j]
            if len(value) == length:
                sub.add(value)  # Add the substring to the set
                break
    print(*sub)  # Print the substrings
    return ''

# Call the substring function with the input word, index, and length, and print the resulting substrings
print(substring(w, i, l))
