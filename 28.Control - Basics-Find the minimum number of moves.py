# Find the minimum number of moves

t = 10  # Set the value of t to 10

for i in range(t):  # Loop 10 times
    a, b = map(int, input().split())  # Read two integer inputs, a and b, from the user

    if a == b:  # Check if a is equal to b
        print(0)  # If they are equal, print 0
    else:
        greater = max(a, b)  # Determine the greater value between a and b
        lesser = min(a, b)  # Determine the lesser value between a and b

        result = (abs(greater - lesser) // 10) + (1 if abs(greater - lesser) % 10 > 0 else 0)
        print(result)
        # Calculate the absolute difference between greater and lesser, divide it by 10,
        # and add 1 if the modulo 10 of the difference is greater than 0.
        # Print the result.

    break  # Exit the loop after the first iteration

