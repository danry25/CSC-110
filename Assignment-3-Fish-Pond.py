# Dan Ryan
# Assignment 3: Fish Pond
# Challenge
# Calculating the dimensions & volume of fish ponds

import sys
import math

DIMENSIONS_CIRCLE = [5]
DIMENSIONS_SQUARE = [5]
DIMENSIONS_RECTANGLE = [4, 7]
DIMENSIONS_OVAL = [4, 6]
DIMENSIONS_L = [3, 6, 5, 10]

print("Fish ponds are available in the following shapes:")  # request, store & validate pond shape
print("  circle, square, rectangle, oval, L")
pondShape = input("Please select the shape for your fish pond: ")
if pondShape in ['circle', 'square', 'rectangle', 'oval', 'L']:
    pass
else:
    print("\nUnrecognized shape \"{}\".".format(pondShape))
    print("Please run the program again.")
    sys.exit(0)

print("Fish ponds are available in the following depths:")  # request, store & validate pond depth
print("  18, 24, 30")
pondDepth = input("Please select the depth for your fish pond: ")
if pondDepth in ['18', '24', '30']:
    depth = int(pondDepth) / 12  # This should prolly go around line 36?
else:
    print("\nUnrecognized depth \"{}\".".format(pondDepth))
    print("Please run the program again.")
    sys.exit(0)

# Calculate pond dimensions
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
    x = DIMENSIONS_RECTANGLE[0]
    y = DIMENSIONS_RECTANGLE[1]
    baseArea = x * y
    basePerim = (x * 2) + (y * 2)
    sideArea = depth * basePerim
    volume = baseArea * depth
    surfaceArea = baseArea + sideArea
    borderArea = ((x + 4) * (y + 4)) - baseArea
elif pondShape == 'oval':
    a = DIMENSIONS_OVAL[1]
    b = DIMENSIONS_OVAL[0]/2
    c = DIMENSIONS_OVAL[0]
    baseArea = (b * c) + (math.pi * (b ** 2))
    basePerim = 2 + 2 + (math.pi * c)
    sideArea = depth * basePerim
    volume = baseArea * depth
    surfaceArea = baseArea + sideArea
    borderArea = ((b * (c + 4)) + (math.pi * (b + 2) ** 2)) - baseArea
elif pondShape == 'L':
    a = DIMENSIONS_L[0]
    b = DIMENSIONS_L[1]
    c = DIMENSIONS_L[2]
    d = DIMENSIONS_L[3]
    baseArea = (a * (d - c)) + (b * c)
    basePerim = (b + d) * 2
    sideArea = depth * basePerim
    volume = baseArea * depth
    surfaceArea = baseArea + sideArea
    borderArea = (14 * 4) + (6 * 4)

# Output the pond dimensions to the user
print("\nThe volume of your fish pond is {:.3f} cubic feet.".format(volume))
print("The surface area of your fish pond is {:.3f} square feet.".format(surfaceArea))
print("The area of the border is {:.3f} square feet.".format(borderArea))
