# Using functions, Find the product

# Define the function 'product' that takes two arguments 'a' and 'b'
def product(a, b):
    pro = a * b  # Calculate the product of 'a' and 'b'
    return pro  # Return the calculated product

# Prompt the user to input two integers 'n1' and 'n2'
n1 = int(input())
n2 = int(input())

# Call the 'product' function with 'n1' and 'n2' as arguments and print the result
print(product(n1, n2))
