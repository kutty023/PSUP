# Print all vowels

word = input()  # Read a string input from the user and store it in the variable word

for i in word:  # Iterate over each character in the word
    if i in 'aeiou':  # Check if the character is a vowel ('a', 'e', 'i', 'o', or 'u')
        print(i, end='')  # If it is a vowel, print the vowel character without a newline