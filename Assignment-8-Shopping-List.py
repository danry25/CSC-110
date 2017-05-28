# Dan Ryan
# Assignment 8: Shopping List
# Challenge
# Creating and maintaining a shopping list

# create a shared list
theList = []


# Prints menu of stuff our program can do
def printMenu():
    print("Here are the list of commands:")
    print("  -p : Print the List")
    print("  -e : Empty the List")
    print("  -x : Exit")
    print("  -h : Print this command list")


# Adds an item to the list if it isn't in the list already
def addToList(item):
    # Check if item is on shopping list
    if item not in theList:
        # Add item to list
        theList.append(item)
        # Tell user item is on list
        print("'{}'' added to the list.".format(item))
    # Tell user that item is already on list
    else:
        print("'{}' is already on the list".format(item))


# Ask for user input
def getInput():
    # Tell user how many items are on the list
    print('You have {} items on your list.'.format(len(theList)))
    # Prompt for user action
    return input('Enter an item or command: ')


def printList():
    count = 1
    print('Your shopping list:')
    for x in theList:
        print("  {}.".format(count), x)
        count += 1


# Start emptying the list
def emptyList():
    # Go through list and remove each item
    while len(theList) > 0:
        theList.pop()


def removeFromList(item):
    try:
        itemNum = int(item) - 1
        theList.remove(theList[itemNum])
        print("Item {} removed from the list.".format(theList[itemNum]))
    except:
        theList.remove(item)
        print("Item {} removed from the list.".format(item))
    print(item)


def startProgram():
    print('Welcome to the XYZ Shopping List Program')


def endProgram():
    print('Thank you for using the XYZ Shoppling List Program.')


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
        elif '-r ' in item:
            item = item.lstrip('-r ')
            removeFromList(item)
        elif item == '':
            print()
        else:
            addToList(item)
        item = getInput()
    endProgram()


main()