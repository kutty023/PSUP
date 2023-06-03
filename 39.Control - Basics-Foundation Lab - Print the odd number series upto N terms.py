# Print the odd number series upto N terms

n = int(input())  # Read an integer input from the user and store it in variable n

for i in range(1, 2*n):  # Iterate over the range of numbers from 1 to 2n (exclusive)
    if i % 2 != 0:  # Check if the number i is odd by checking if the remainder of i divided by 2 is not equal to 0
        print(i, end=' ')  # If i is odd, print i followed by a space without a newline
