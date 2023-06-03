# Longest Common Prefix in a String

n = int(input())  # Take an integer input
w = list(input().split())[:n]  # Take a list of strings as input

def prefix(x):
    if not x:
        return ''  # If the input list is empty, return an empty string

    pre = x[0]  # Initialize the prefix variable with the first string in the list

    for i in x[1:]:
        while pre != i[:len(pre)]:  # Compare the prefix with each string in the list
            pre = pre[:len(pre)-1]  # Remove the last character from the prefix
            if not pre:
                return ""  # If the prefix becomes empty, return an empty string

    return pre  # Return the common prefix found among all strings

print(prefix(w))  # Print the common prefix
