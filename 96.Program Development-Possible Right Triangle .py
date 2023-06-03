# Possible Right Triangle

P = int(input())  # Prompt the user to enter the perimeter value and store it in the variable P.

# Check if it is possible to form a right-angled triangle
def isRightAngledTriangle(perimeter):
    for a in range(1, perimeter//2):  # Iterate over possible values of side a, ranging from 1 to half of the perimeter (perimeter//2).
        for b in range(a, perimeter//2):  # Iterate over possible values of side b, ranging from the current value of a to half of the perimeter.
            c = perimeter - a - b  # Calculate the value of side c based on the given perimeter and values of sides a and b.
            if a*a + b*b == c*c:  # Check if the Pythagorean theorem is satisfied (a^2 + b^2 = c^2).
                return True  # If a right-angled triangle is found, return True.

    return False  # If no right-angled triangle is found, return False.

# Check if it is possible to form a right-angled triangle with given perimeter
if isRightAngledTriangle(P):
    print("Yes")  # Print "Yes" if a right-angled triangle can be formed.
else:
    print("No")  # Print "No" if a right-angled triangle cannot be formed.
