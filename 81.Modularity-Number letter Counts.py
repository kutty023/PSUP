# Number letter Counts

# Take an input string 'n'
n = input()

value = 0

# Iterate over each character in 'n'
for i in n:
    i = int(i)  # Convert the character to an integer
    
    # Check the value of 'i' and update 'value' accordingly
    if i == 1 or i == 2 or i == 6:
        value += 3
    elif i == 3 or i == 7 or i == 8:
        value += 5
    else:
        value += 4

print(value)  # Print the calculated 'value'


# Actual input
# Take an integer input 'number'
number = int(input())

# Define a function to calculate the strokes for each digit
def word(n):
    if n == 1 or n == 2 or n == 6:
        return 3
    elif n == 3 or n == 7 or n == 8:
        return 5
    elif n == 0 or n == 4 or n == 5 or n == 9:
        return 4

# Define a function to calculate the sum of strokes for the number
def sum(num):
    s = 0
    while num > 0:
        ele = num % 10
        s += word(ele)
        num = int(num / 10)
    return s

# Print the sum of strokes for the number
print(sum(number))
