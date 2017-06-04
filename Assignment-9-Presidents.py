# Dan Ryan
# Assignment 9: Presidents
# Challenge
# Parse text file and create new files with data ordered by date, name, etc.


def fileParser(inFile):
    pres = []
    try:
        # Open and parse requested file
        unparsedFile = open(inFile)
        # Process line into variable
        line = unparsedFile.readline()
        # Loop through each line and process it into separatedWords
        while line != "":
            lineParsed = line.strip().split("\t")
            if not len(lineParsed) == 5:
                pres.append(lineParsed[1] + ' ' + lineParsed[0])
                pres.append(lineParsed[2])
                pres.append(lineParsed[3])
            else:
                pres.append(lineParsed[2] + ' ' + lineParsed[1] + ' ' + lineParsed[0])
                pres.append(lineParsed[3])
                pres.append(lineParsed[4])

            # Read next line
            line = unparsedFile.readline()
        unparsedFile.close()
        return pres
    except:
        # If input file doesn't exist, complain and exit
        print('Input file {} could not be read :c'.format(inFile))


def sameOrder(pres):
    meter = pres[::3]
    counter = 0
    data = []
    for thing in meter:
        data.append(thing + ' was president from ' + pres[1+counter] + ' to ' + pres[2+counter] + '.' '\n')
        counter += 3
    return data


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


def main():
    pres = fileParser('presidents.txt')
    same = sameOrder(pres)
    fileWriter('same_order.txt', same)


main()
