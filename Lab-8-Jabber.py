# Dan Ryan
# Lab 8: Jabber
# Plus
# Find some words containing a string in a file

# Bring in sys.argv to handle runtime options
import sys.argv as userarg

# Open, read & parse file into an array so we can work with it
jf = open('jabber.txt', 'r')

# Loop through each item in array
for word in jf:
    # Check if there are any duplicates in the array
    if word in jf():
        pass
