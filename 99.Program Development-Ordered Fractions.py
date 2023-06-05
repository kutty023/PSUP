# Ordered Fractions

a, b = map(int, input().split())  # Take input and assign the values of a and b accordingly.
c = min(a, b)  # Determine the smaller value between a and b and store it in c.

if a == 1 or b == 1:
    print("-1")  # If either a or b is 1, the fraction is already in its simplest form, so we print -1.
else:
    for i in range(2, c + 1):  # Iterate from 2 to the smaller value between a and b.
        if a % i == 0 and b % i == 0:  # Check if both a and b are divisible by i.
            print(f"{int(a / i)}/{int(b / i)}", end=" ")  # Print the reduced form of the fraction.

