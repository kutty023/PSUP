# Sum of extracted digits

# Take input for n1 and n2
n1 = int(input())
n2 = int(input())

# Check if either number is less than 10
if (n1<10 or n2<10):
    # If either number is less than 10, print an error message
    print("Invalid number")
else:
    # If both numbers are greater than or equal to 10, proceed with the calculation
    # Divide n1 and n2 by 10 to extract the tens digit
    digit1 = n1/10
    digit2 = n2/10

    # Take the modulo of the result with 10 to get the ones digit
    # and add the ones digits together to get the sum
    sum = (digit1%10) + (digit2%10)

    # Print the sum as an integer
    print(int(sum))
