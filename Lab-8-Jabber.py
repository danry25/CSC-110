# Dan Ryan
# Lab 8: Jabber
# Plus
# Find some words containing a string in a file

# Bring in sys.argv to handle runtime options
# import sys.argv as userarg

# Open, read & parse file into an array so we can work with it
jf = open('jabber.txt', 'r')
# Open jabber-selected-words.txt for writing
jswf = open('jabber-selected-words.txt', 'w')

# Loop through each item in array
for word in jf:
    # Check if there are any duplicates in the array
    if word in jf:
        pass


# read a line from jabber.txt
line = jf.readline()

# while there are still lines to be read:
while line != '':
    print("holla")
    # check if the line contains a 'j':
    if 'j' in line:
        # if it does, write it to jabber-selected-words.txt
        jswf.append(line)
        print(line)
    # read the next line from jabber.txt
    line = jf.readline()

# close the files
jf.close()
jswf.close()

print(line)
