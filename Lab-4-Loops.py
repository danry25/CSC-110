# Dan Ryan
# Lab 4: Loops
# Plus
# This script counts to 280 in increments of 31 in multiple ways

# Create a couple baseline variables & lists
whileLoop = 1
whileList = []
forList = []
forRange = []
oneArg = []

print("Using the while loop:")  # Generate output using a while loop & basic addition

while whileLoop < 281:  # Limits to 280 as max value before halting
    whileList.append(str(whileLoop))  # formats and adds data to list
    whileLoop = whileLoop + 31

print(", ".join(whileList))  # Outputs nicely formatted stuff to user


print("\nUsing the for loop with a list:")  # This one literally outputs a pre-defined list

for i in [1, 32, 63, 94, 125, 156, 187, 218, 249, 280]:
    forList.append(str(i))  # Formats the item and adds it to a new list, so this isn't 100% pointless :P

print(", ".join(forList))  # Outputs nicely formatted stuff to user

# This does 24 thru 27 in one line. Commenting out as it doesn't fit what the goal of this lab is.
# print(", ".join(repr(i) for i in forList))


print("\nUsing the for loop with range, three argument:")  # Loop & range based solution, with range doing heavy lifting

for i in range(1, 281, 31):
    forRange.append(str(i))

print(", ".join(forRange))  # print output for uert


print("\nUsing the for loop with range, one argument:")  # Heavy lifting here is done using basic multiplication

for i in range(10):
    loopRange = (i * 31) + 1
    oneArg.append(str(loopRange))

print(", ".join(oneArg))  # Outputs nicely formatted stuff to user
