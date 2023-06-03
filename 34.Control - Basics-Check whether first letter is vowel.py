# Check whether first letter is vowel

word = str(input())  # Read a string input from the user and store it in the variable word

if word[0] in 'aeiou':  # Check if the first character of the word is a vowel
    print("Yes")  # If it is, print "Yes" to indicate that the first letter is a vowel
else:
    print("No")  # If the first character is not a vowel, print "No" to indicate that the first letter is not a vowel
