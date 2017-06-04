

def twentyval():
    # declare an array that can hold 20 integer values
    storage = []
    # use a loop to put the integer values 1, 2, 3, ..., 18, 19, 20 into the array
    for num in range(20):
        storage.append(num + 1)
    return storage


def helper(twenty):
    total = 0
    print(twenty)
    for num in twenty:
        if not num % 2 == 0:
            print(num)
            total += num


def main():
    twenty = twentyval()
    # pass the array to the helper function which will return an integer value
    total = helper(twenty)
    # print out the value returned by the helper function
    print(total)


main()
