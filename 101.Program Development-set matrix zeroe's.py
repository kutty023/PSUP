# set matrix zeroe's

m, n = map(int, input().split())  # Input the dimensions of the matrix

# Create the matrix
matrix = []
for i in range(m):
    row = list(map(int, input().split()))[:n]  # Input each row of the matrix
    matrix.append(row)

# Find the positions of 0 elements
zero_rows = set()  # Set to store row indices with 0 elements
zero_cols = set()  # Set to store column indices with 0 elements
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            zero_rows.add(i)  # Add the row index to zero_rows set
            zero_cols.add(j)  # Add the column index to zero_cols set

# Set row and column to 0 if there is a zero element
for i in range(m):
    for j in range(n):
        if i in zero_rows or j in zero_cols:
            matrix[i][j] = 0  # Set the element to 0 if its row or column index is in zero_rows or zero_cols

# Print the modified matrix
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=" ")  # Print each element of the matrix
    print()  # Move to the next line after printing each row
