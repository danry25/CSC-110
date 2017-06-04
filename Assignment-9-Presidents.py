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
                pres.append(lineParsed[0])
            else:
                pres.append(lineParsed[2] + ' ' + lineParsed[1] + ' ' + lineParsed[0])
                pres.append(lineParsed[3])
                pres.append(lineParsed[4])
                pres.append(lineParsed[0])

            # Read next line
            line = unparsedFile.readline()
        unparsedFile.close()
        return pres
    except:
        # If input file doesn't exist, complain and exit
        print('Input file {} could not be read :c'.format(inFile))


def sameOrder(pres):
    meter = pres[::4]
    counter = 0
    data = []
    for thing in meter:
        data.append(thing + ' was president from ' + pres[1+counter] + ' to ' + pres[2+counter] + '.' '\n')
        counter += 4
    return data


def lastName(pres):
    meter = pres[::4]
    counter = 0
    orgData = []
    data = []
    orgData = sorted(pres, key=lambda president: president[3])
    print(orgData)
    for thing in meter:
        data.append(orgData[counter] + ' was president from ' + orgData[1+counter] + ' to ' + orgData[2+counter] + '.' '\n')
        counter += 4
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


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
        
    def __repr__(self):
         return repr((self.name, self.grade, self.age))


def main():
    pres = fileParser('presidents.txt')
    same = sameOrder(pres)
    fileWriter('same_order.txt', same)
    last = lastName(pres)
    fileWriter('last_name.txt', last)
    # inauguration.txt


main()
