# Dan Ryan
# Assignment 8: Shopping List
# Challenge
# Creating and maintaining a shopping list

# create a shared list
theList = []
# Open storage file
try:
    SHOPPING = open('shopping-list.txt')
except:
    # If storage file doesn't exist, create it
    open('shopping-list.txt', 'w')
    SHOPPING = open('shopping-list.txt')


# Prints menu of stuff our program can do
def printMenu():
    print("Here are the list of commands:")
    print("  -p : Print the List")
    print("  -e : Empty the List")
    print("  -r item : Removes item from list")
    print("  -x : Exit")
    print("  -h : Print this command list")


# Adds an item to the list if it isn't in the list already
def addToList(item):
    # Check if item is on shopping list
    if item not in theList:
        # Add item to list
        theList.append(item)
        # Tell user item is on list
        print("'{}' added to the list.".format(item))
    # Tell user that item is already on list
    else:
        print("'{}' is already on the list".format(item))


# Ask for user input
def getInput():
    # Tell user how many items are on the list
    print('You have {} items on your list.'.format(len(theList)))
    userinput = ''
    usertry = False
    while userinput == '':
        # Check if the user has tried before
        if usertry:
            print("Shopping list items cannot be blank")
        # Prompt for user action
        userinput = input('Enter an item or command: ')
        # Mark user as having given blank input
        usertry = True
    # Throw this data back to the relevant function
    return userinput


# Print the list for the user
def printList():
    count = 1
    print('Your shopping list:')
    # Print off each item in the list
    for x in theList:
        print("  {}.".format(count), x)
        # Enumerate our way for each item on the list, eg 1. Thing, 2. Stuff
        count += 1


# Start emptying the list
def emptyList():
    # Go through list and remove each item
    while len(theList) > 0:
        theList.pop()


# Give the user a way to prune their shopping list
def removeFromList(item):
    # Trim away -r by trashing the first 3 chars
    item = item[3:]
    # Remove the item if they gave its string
    try:
        theList.remove(item)
        print("Item {} removed from the list.".format(item))
    # Try a few other ways of removing the item if its string didn't match in the array
    except:
        try:
            itemNum = int(item) - 1
            # Reject negative numbers
            if '-' in item:
                print("'{}'could not be located, index starts at 1".format(item))
            # Remove item by item number
            else:
                itemStr = theList[itemNum]
                theList.remove(itemStr)
                print("Item {} removed from the list.".format(itemStr))
        # Complain to user if we can't find an item string or number that matches
        except:
            print("'{}'could not be located".format(item))


# Initiate the program
def startProgram():
    print('Welcome to the XYZ Shopping List Program')
    # Loop through each line and process it into theList
    line = SHOPPING.readline()
    while line != "":
        theList.append(line.rstrip('\n'))
        line = SHOPPING.readline()


# End the program
def endProgram():
    print('Thank you for using the XYZ Shoppling List Program.')
    # Write shopping list to disk
    SH = open('shopping-list.txt', 'w')
    for thing in theList:
        SH.write(thing + '\n')
    # Close files
    SH.close()
    SHOPPING.close()


# Main function, kicks off other functions depending on what the user inputs
def main():
    startProgram()
    printMenu()
    item = getInput()
    while item != '-x':
        if item == '-p':
            printList()
        elif item == '-h':
            printMenu()
        elif item == '-e':
            emptyList()
        elif "-r " in item:
            removeFromList(item)
        elif item[0] == "-":
            print("Sorry, your command was unrecognized. Try -h for help!")
        else:
            addToList(item)
        item = getInput()
    endProgram()


# Call main function to start the program
main()
