# Two sum

l = list(map(int, input().split()))  # Input a list of integers
t = int(input())  # Input the target sum

for i in range(0, len(l) - 1):  # Iterate over the list, except the last element
    s = l[i] + l[i + 1]  # Calculate the sum of current element and the next element
    if s == t:  # Check if the sum is equal to the target sum
        print(i, i + 1, sep=',')  # Print the indices of the elements that form the target sum