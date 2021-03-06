# Dan Ryan
# Assignment 6: There was an Old Lady
# Challenge
# Returns a song about an old lady to the user


# prints title
def title():
    print('There was an Old Lady\n')


# prints initial swallowed line
def swallowed(animal, punctuation):
    print ("There was an old lady who swallowed a {}{}".format(animal, punctuation))


# prints that she swallowed another animal to catch prior animal swallowed
def swallowedCatch(animal, animal2, punctuation):
    print("She swallowed the {} to catch the {}{}".format(animal, animal2, punctuation))


# Prints 2 lines in each stanza, 4 lines before end of stanza
def wriggled():
    print("That wriggled and jiggled and tickled inside her.")
    print("She swallowed the spider to catch the fly.")


# Prints final 2 lines in each stanza
def dontKnowWhy():
    print("I don't know why she swallowed the fly.")
    print("Perhaps she'll die.\n")


# Below is each verse, 1 through 6 & lastverse
def verse1():
    swallowed("fly", ".")
    dontKnowWhy()


def verse2():
    swallowed("spider", ",")
    wriggled()
    dontKnowWhy()


def verse3():
    swallowed("bird", ".")
    print("How absurd to swallow a bird.")
    swallowedCatch("bird", "spider", ",")
    wriggled()
    dontKnowWhy()


def verse4():
    swallowed("cat", ".")
    print("Imagine that to swallow a cat.")
    swallowedCatch("cat", "bird", ".")
    swallowedCatch("bird", "spider", ",")
    wriggled()
    dontKnowWhy()


def verse5():
    swallowed("dog", ".")
    print("My, what a hog, to swallow a dog.")
    swallowedCatch("dog", "cat", ".")
    swallowedCatch("cat", "bird", ".")
    swallowedCatch("bird", "spider", ",")
    wriggled()
    dontKnowWhy()


def verse6():
    swallowed("hawk", ".")
    print("It would be a site to see, for her to swallow a hawk.")
    swallowedCatch("hawk", "dog", ".")
    swallowedCatch("dog", "cat", ".")
    swallowedCatch("cat", "bird", ".")
    swallowedCatch("bird", "spider", ",")
    wriggled()
    dontKnowWhy()


def lastverse():
    swallowed("horse", ".")
    print("She's dead, of course.")


# Main function, causes all the other functions to actually run!
def main():

    # print the title
    title()

    # fly verse
    verse1()

    # spider verse
    verse2()

    # bird verse
    verse3()

    # cat verse
    verse4()

    # dog verse
    verse5()

    # new verse
    verse6()

    # horse verse
    lastverse()


# call main
main()
