# Dan Ryan
# Lab 9: Making Jabber.txt
# Plus
# Split up words in a file onto separate lines

# Bring in sys.argv to handle runtime options
import sys
# Use OS to check if file exists
import os
# Create a list to store bits of the file
separatedWords = []


def fileParser(inFile):
    try:
        # Open and parse requested file
        unparsedFile = open(inFile)
        # Process line into variable, skip first 4 lines
        line = unparsedFile.readline()
        line = unparsedFile.readline()
        line = unparsedFile.readline()
        line = unparsedFile.readline()
        line = unparsedFile.readline()
        # Loop through each line and process it into separatedWords
        while line != "":
            lineParsed = line.strip().split(" ")
            for thing in lineParsed:
                # Check if line is blank, skip if its blank, append otherwise
                if thing != '':
                    separatedWords.append(thing)
                else:
                    pass
            # Read next line
            line = unparsedFile.readline()
    except:
        # If input file doesn't exist, complain and exit
        print('Input file {} could not be read :c'.format(inFile))


def fileWriter(outFile):
    try:
        # Write parsed list to disk
        parsedFile = open(outFile, 'w')
        for thing in separatedWords:
            parsedFile.write(thing + '\n')
        # Close files
        parsedFile.close()
    except:
        # If file isn't writable/openable, complain to user
        print('Could not open or write to {}, check your file permissions.'.format(outFile))


# Main function that handles user input & calls the other functions
def main():
    # Check if 2 arguments passed, and see if 2nd argument is a file - Could use a try except alternatively
    if len(sys.argv) == 3 and not os.path.isfile(sys.argv[2]):
        fileParser(sys.argv[1])
        fileWriter(sys.argv[2])
    # Handle all other conditions where arguments are passed
    elif len(sys.argv) >= 2:
        # Clean out data from list
        files = sys.argv
        files.remove(files[0])
        for inFile in files:
            while len(separatedWords) != 0:
                separatedWords.pop()
            fileParser(inFile)
            outFile = inFile.replace('.txt', '-out.txt')
            fileWriter(outFile)
    # If no arguments were passed, just process the default file
    else:
        fileParser('jabberwocky.txt')
        fileWriter('jabber-out.txt')


# Run the main functions
main()
