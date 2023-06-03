# Print the factors of a given number

n = int(input())  # Takes an input from the user and converts it to an integer, storing it in the variable 'n'.

for i in range(1, n+1):
    # The 'range()' function creates a sequence of numbers from 1 to n (inclusive) and assigns each value to the variable 'i' one at a time.
    # The loop will iterate 'n' times, with 'i' taking the values 1, 2, 3, ..., n.

    if (n % i == 0):
        # The '%' operator calculates the remainder of the division between 'n' and 'i'.
        # If the remainder is 0, it means 'i' is a factor of 'n'.
        # In other words, 'i' divides 'n' without leaving any remainder.

        print(i, end=",")
        # If 'i' is a factor of 'n', it will be printed.
        # The 'end=','' argument ensures that the output is separated by commas instead of newlines.
