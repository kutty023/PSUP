# Fizz buzz

num = int(input())  # Read an integer input from the user and store it in num

for n in range(1, num+1):  # Iterate over numbers from 1 to num (inclusive)
    if n % 15 == 0:  # Check if the number is divisible by both 3 and 5
        print("FizzBuzz", end=' ')  # If it is, print "FizzBuzz" without a newline
        continue  # Continue to the next iteration of the loop

    elif n % 3 == 0:  # Check if the number is divisible by 3
        print("Fizz", end=' ')  # If it is, print "Fizz" without a newline
        continue  # Continue to the next iteration of the loop

    elif n % 5 == 0:  # Check if the number is divisible by 5
        print("Buzz", end=' ')  # If it is, print "Buzz" without a newline
        continue  # Continue to the next iteration of the loop

    else:
        print(n, end=' ')  # If the number is not divisible by 3 or 5, print the number itself without a newline
