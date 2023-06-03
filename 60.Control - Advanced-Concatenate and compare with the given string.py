# Concatenate and compare with the given string

# Take input for str1 and str2 separated by a space
str1, str2 = input().split()

# Take input for str3
str3 = input()

# Concatenate str1 and str2
con = str1 + str2

# Compare con with str3
if con == str3:
    print("Yes")
else:
    print("No")
