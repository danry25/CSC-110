# Dan Ryan
# Lab 9: Making Jabber.txt
# Plus
# Split up words in a file onto separate lines

separatedWords = []


def fileParser(inFile):
    try:
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
                if thing != '':
                    separatedWords.append(thing)
                else:
                    pass
            line = unparsedFile.readline()
    except:
        # If input file doesn't exist, complain and exit
        print('Input file could not be read :c')


def fileWriter(outFile):
        # Write parsed list to disk
        parsedFile = open(outFile, 'w')
        print(separatedWords)
        for thing in separatedWords:
            parsedFile.write(thing + '\n')
        # Close files
        parsedFile.close()


def emptyList():
    # Go through list and remove each item
    while len(separatedWords) > 0:
        separatedWords.pop()


def doStuff():
    fileParser('jabberwocky.txt')
    fileWriter('jabber-out.txt')


doStuff()
