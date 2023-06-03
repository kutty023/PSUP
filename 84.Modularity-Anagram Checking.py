# Anagram Checking

# Take input of two strings 's' and 't'
s, t = input().split()

# Define a function to check if two strings are anagrams
def isAnagram(a, b):
    # Sort the characters in strings 'a' and 'b'
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    # Check if the sorted strings are equal
    if sorted_a == sorted_b:
        return 1  # If equal, strings are anagrams
    else:
        return 0  # If not equal, strings are not anagrams

# Call the isAnagram function with 's' and 't' as arguments and print the result
print(isAnagram(s, t))
