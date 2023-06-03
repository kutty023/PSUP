# print  the power digit sum

# Take an integer input 'n'
n = int(input())

if n > 0 and n <= 16:  # Check if 'n' is within the range (1 to 16)
    pow = 2 ** n  # Calculate 2 raised to the power of 'n'
    Pow = str(pow)  # Convert 'pow' to a string
    sum = 0  # Initialize the 'sum' variable to 0

    # Iterate over each character 'i' in the string 'Pow'
    for i in Pow:
        sum += int(i)  # Add the integer value of 'i' to 'sum'

print(sum)  # Print the value of 'sum'


# Actual input
# Take an integer input 'num'
num = int(input())

def powersum(n):
    power = 0
    
    if n <= 0:
        return -1  # Return -1 if 'n' is less than or equal to 0
    elif n > 0 and n <= 16:
        power = 2 ** n  # Calculate 2 raised to the power of 'n'
    
    sum = 0
    
    # Calculate the sum of digits in 'power'
    while power != 0:
        sum += int(power % 10)  # Add the last digit to 'sum'
        power = int(power / 10)  # Remove the last digit from 'power'
    
    return sum  # Return the calculated sum

print(powersum(num))  # Call the 'powersum' function with 'num' as argument and print the result

