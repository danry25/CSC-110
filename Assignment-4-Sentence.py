# Dan Ryan
# Assignment 4: Sentence Statistics
# Challenge
# This script calculates statistics on sentences that were inputted by the user.

while True:
    # set up variables for counts
    charCount = 0
    letterCount = 0
    upperCount = 0
    lowerCount = 0
    digitCount = 0
    spaceCount = 0
    wordCharCount = 0
    punctCount = 0
    wordsCount = 0
    currentlyInWord = False
    # get a sentence from the user
    sentence = input('Enter a sentence (return to exit): ')
    # loop through the sentence
    if sentence == "":
        print("Good-bye.")
        break
    for char in sentence:
        # count the characters
        charCount = charCount + 1
        if char.isspace():
            spaceCount += 1
            currentlyInWord = False
        # count the digits
        elif char.isdigit():
            digitCount += 1
        # count the letters
        elif char.isalpha():
            letterCount += 1

        # count the upper-case letters
        if char.isupper():
            upperCount += 1
        # count the lower-case letters
        elif char.islower():
            lowerCount += 1
        # count word characters
        elif char in "@#$%&+-=<>*/":
            wordCharCount += 1
            currentlyInWord = False
        elif char in "!~`^()_{}[]|\\;:\"',.?":
            punctCount += 1
            currentlyInWord = False
        if char.isalnum() and not currentlyInWord:
            currentlyInWord = True
            wordsCount += 1

    # print out the counts
    print('Statistics on your sentence: ')
    print('   Characters:', charCount)
    print('   Letters:', letterCount)
    print('   Upper-case:', upperCount)
    print('   Lower-case:', lowerCount)
    print('   Digits:', digitCount)
    print('   Spaces:', spaceCount)
    print('   Word characters:', wordCharCount)
    print('   Punctuation:', punctCount)
    print('   Words:', wordsCount)
    # print out a blank line
    print()
