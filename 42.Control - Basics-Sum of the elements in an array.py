# Sum of the elements in an array

n = int(input())  # Read an integer input from the user and store it in the variable n
a = list(map(int, input().split()))[:n]  # Read a list of integers from the user, split by space, convert each element to integer, and store the first n elements in the list a
print(sum(a))  # Calculate the sum of the elements in the list a using the sum() function and print the result
