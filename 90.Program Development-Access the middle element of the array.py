# Access the middle element of the array

n = int(input())  # Take input for the number of elements in the list

arr = list(map(int, input().split()))[:n]  # Take input for the list of integers

N = n // 2  # Calculate the index N using integer division

print(arr[N])  # Print the value at index N in the list arr
