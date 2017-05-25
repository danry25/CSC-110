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
jsw = []

# read a line from jabber.txt
line = jf.readline()
chars = 'j'

# While there are still lines to be read:
while line != '':
    if line not in jsw:
        jsw.append(line)
            print(line, end=' ')
        # read the next line from jabber.txt
        line = jf.readline()


# Check if the line contains a letter:
for letter in 'abcdefghijklmnopqrstuvwxyz':
    chars = letter
    if chars in jsw:
        # if it does, write it to jabber-selected-words.txt
        jswf.write(line)
        # Then strip the newline bit
        line = line.strip('\n')
        # Append it to the array to be printed
        jsw.append(line)
        print(line, end=' ')
    elif chars.upper() in line:
        # if it does, write it to jabber-selected-words.txt
        jswf.write(line)
        # Then strip the newline bit
        line = line.strip('\n')
        # Append it to the array to be printed
        jsw.append(line)

# close the files
jf.close()
jswf.close()

for thing in jsw:
    print(thing)
