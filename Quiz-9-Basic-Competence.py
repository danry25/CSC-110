

# Sums odd values in array
def helper(twenty):
    # Running total
    total = 0
    for num in twenty:
        # If the number is odd,  this is triggered
        if not num % 2 == 0:
            # Add current number to total
            total += num
    # Throw sum back to main
    return total


# Main function which calls all the helper functions
def main():
    # declare an array that can hold 20 integer values
    storage = []
    # use a loop to put the integer values 1, 2, 3, ..., 18, 19, 20 into the array
    for num in range(20):
        # appends to array here, adding 1 to get correct values
        storage.append(num + 1)
        # Throws data back to main for later use
    # pass the array to the helper function which will return an integer value
    total = helper(storage)
    # print out the value returned by the helper function
    print(total)


# Call main so it will actually be ran :P
main()
