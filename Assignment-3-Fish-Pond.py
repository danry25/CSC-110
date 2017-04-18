# Dan Ryan
# Assignment 3: Fish Pond
# Challenge
# Calculating the dimensions & volume of fish ponds

import sys
import math

DIMENSIONS_CIRCLE = [5]
DIMENSIONS_SQUARE = [5]
DIMENSIONS_rectangle = [4, 7]
DIMENSIONS_OVAL = [4, 6]
DIMENSIONS_L = [3, 6, 5, 10]

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
    depth = int(pondDepth) / 12  # This should prolly go around line 36?
else:
    print("\nUnrecognized depth \"{}\".".format(pondDepth))
    print("Please run the program again.")
    sys.exit(0)


if pondShape == 'circle':
    radius = DIMENSIONS_CIRCLE[0]/2
    baseArea = math.pi * radius ** 2
    basePerim = 2 * math.pi * radius
    sideArea = depth * basePerim
    volume = baseArea * depth
    surfaceArea = baseArea + sideArea  # I kinda wanna spin this and line 48 off on line 53
    borderArea = (math.pi * (radius + 2) ** 2) - baseArea
elif pondShape == 'square':
    sideLength = DIMENSIONS_SQUARE[0]
    baseArea = sideLength ** 2
    basePerim = sideLength * 4
    sideArea = depth * basePerim
    volume = baseArea * depth
    surfaceArea = baseArea + sideArea
    borderArea = ((sideLength + 4) ** 2) - baseArea
elif pondShape == 'rectangle':
    x = DIMENSIONS_rectangle[0]
    y = DIMENSIONS_rectangle[1]
    baseArea = x * y
    basePerim = (x * 2) + (y * 2)
    sideArea = depth * basePerim
    volume = baseArea * depth
    surfaceArea = baseArea + sideArea
    borderArea = ((x + 4) * (y + 4)) - baseArea


print("\nThe volume of your fish pond is {:.3f} cubic feet.".format(volume))
print("The surface area of your fish pond is {:.3f} square feet.".format(surfaceArea))
print("The area of the border is {:.3f} square feet.".format(borderArea))
