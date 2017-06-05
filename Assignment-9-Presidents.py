# Dan Ryan
# Assignment 9: Presidents
# Challenge
# Parse text file and create new files with data ordered by date, name and inauguration.

# Nab datetime so we can deal with super specific time/date info
from datetime import datetime


# Parses files based on input when called
def fileParser(inFile):
    pres = []
    try:
        # Open and parse requested file
        unparsedFile = open(inFile)
        # Process line into variable
        line = unparsedFile.readline()
        # Loop through each line and process it into separatedWords
        while line != "":
            # Split each line up into usable chunks
            lineParsed = line.strip().split("\t")
            # Append it to pres so we can use it later...
            pres.append({
                "firstName": lineParsed[1],
                "lastName": lineParsed[0],
                "start": lineParsed[2],
                "end": lineParsed[3]
            })

            # Read next line
            line = unparsedFile.readline()
        unparsedFile.close()
        return pres
    except:
        # If input file doesn't exist, complain and exit
        print('Input file {} could not be read :c'.format(inFile))


# Formats the sentence and returns it to main
def writeSentence(president):
    return "{firstName} {lastName} was president from {start} to {end}\n".format(**president)


# Creates file with same internal list order
def sameOrder(presidents):
    # Fun inline for loops are fun & unconventional :P
    return [writeSentence(p) for p in presidents]


# Sorts by last name
def lastName(presidents):
    # inline for loop utilizing sorted to sort alphabetically by last name
    return [writeSentence(p) for p in sorted(presidents, key=lambda president: president['lastName'])]


# Sorts by exact inauguration time
def inauguration(presidents):
    # Here I get to use the same for loop and sorted function to sort by date :P Feed me an exact time plz for funziez!
    return [writeSentence(p) for p in sorted(presidents, key=lambda p: datetime.strptime(p['start'], '%m/%d/%Y'))]


# Writes files to disk
def fileWriter(outFile, data):
    try:
        # Write parsed list to disk
        parsedFile = open(outFile, 'w')
        for thing in data:
            parsedFile.write(thing)
        # Close files
        parsedFile.close()
    except:
        # If file isn't writable/openable, complain to user
        print('Could not open or write to {}, check your file permissions.'.format('same_order.txt'))


# Run the functions to process and create the files
def main():
    # Parse the input file
    pres = fileParser('presidents.txt')
    # Output the file in the same order (but beautified)
    same = sameOrder(pres)
    # Write all that good stuff to disk
    fileWriter('same_order.txt', same)
    # Now we sort by last names, wheee!
    last = lastName(pres)
    # Then pass that freshly sorted data to fileWriter and get it on disk
    fileWriter('last_name.txt', last)
    # Here I just decided to call my function inline, then write the output to disk. See, I can save space too!
    fileWriter('inauguration.txt', inauguration(pres))


# Run the main function
main()
