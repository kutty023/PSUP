# Temperature state message

temp = int(input())  # Read an integer temperature value input from the user and store it in temp

if temp < 0:  # Check if the temperature is less than 0
    print("Freezing weather")  # If it is, print "Freezing weather" to indicate very low temperature
elif temp >= 0 and temp < 10:  # Check if the temperature is between 0 (inclusive) and 10 (exclusive)
    print("Very cold weather")  # If it is, print "Very cold weather"
elif temp >= 10 and temp < 20:  # Check if the temperature is between 10 (inclusive) and 20 (exclusive)
    print("Cold weather")  # If it is, print "Cold weather"
elif temp >= 20 and temp < 30:  # Check if the temperature is between 20 (inclusive) and 30 (exclusive)
    print("Normal in temp")  # If it is, print "Normal in temp"
elif temp >= 30 and temp < 40:  # Check if the temperature is between 30 (inclusive) and 40 (exclusive)
    print("It's hot")  # If it is, print "It's hot"
elif temp >= 40:  # Check if the temperature is 40 or greater
    print("It's very hot")  # If it is, print "It's very hot"
