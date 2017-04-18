# Dan Ryan
# Assignment 3: Fish Pond
# Challenge
# Calculating the dimensions & volume of fish ponds

import sys
# import math

print("Fish ponds are available in the following shapes:")
print("  circle, square, rectangle, oval, L")
pondShape = input("Please select the shape for your fish pond: ")  # request, store & validate pond shape
if pondShape in ['circle', 'square', 'rectangle', 'oval', 'L']:
    pass
else:
    print("\nUnrecognized shape \"{}\".".format(pondShape))
    print("Please run the program again.")
    sys.exit(0)

print("Fish ponds are available in the following depths:")
print("  18, 24, 30")
pondDepth = input("Please select the depth for your fish pond: ")  # request, store & validate pond depth
if pondDepth in ['18', '24', '30']:
    pass
else:
    print("\nUnrecognized depth \"{}\".".format(pondDepth))
    print("Please run the program again.")
    sys.exit(0)


print("\nThe volume of your fish pond is 37.500 cubic feet.".format(volume))
print("The surface area of your fish pond is {:.3f} square feet.".format(surfaceArea))
print("The area of the border is {:.3f} square feet.".format(borderArea))
