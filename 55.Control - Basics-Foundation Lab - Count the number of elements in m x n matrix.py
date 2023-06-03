# Count the number of elements in m*n matrix

# Take input for the number of rows and columns
m, n = map(int, input().split())
# Iterate over each row
for i in range(0, m):
    # Iterate over each column
    for j in range(0, n):
        # Print the value 1 followed by a space
        print(1, end=' ')
    # Print a newline character to move to the next row
    print()

