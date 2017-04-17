# Dan Ryan
# Assignment 2: Height Converter
# Challenge
# This script converts heights between imperial and metric units.

import math

print("Please enter the height to be converted.")  # About to gather user input

feet = int(input("First, enter the feet: "))
inches = int(input("Now, enter the inches: "))
totalinches = ((feet * 12) + inches)


# Returning calculations and info to user
print("\nYour height is {} feet {} inches, or {} inches. That is {:.2f} cm.\n".format(totalinches // 12,
                                                                                      totalinches % 12,
                                                                                      totalinches, totalinches * 2.54))

print("Please enter a second height to be converted.")  # About to gather moar user input

centimeters = int(input("Enter the height in centimeters: "))
userinches = (centimeters / 2.54)
eighths = ((userinches + 0.0625) % 1) // .125

# Returning height conversions & info
print("\nYour height is {} cm. That's {:.3f} inches, or {:.0f} feet {:.0f}-{:.0f}/8 inches.".format(centimeters, userinches, (userinches // 12), (math.floor(userinches) % 12), eighths))
