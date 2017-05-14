# Dan Ryan
# Assignment 6: There was an Old Lady
# Challenge
# Returns a song about an old lady to the user


# prints title
def title():
    print('There was an Old Lady\n')


def swallowed(animal, punctuation):
    print ("There was an old lady who swallowed a {}{}".format(animal, punctuation))


def wriggled():
    print("That wriggled and jiggled and tickled inside her.")
    print("She swallowed the spider to catch the fly.")


def dontKnowWhy():
    print("I don't know why she swallowed the fly.")
    print("Perhaps she'll die.\n")


def end():
    print("There was an old lady who swallowed a horse.")
    print("She's dead, of course.")


def verse1():
    swallowed("fly", ".")
    dontKnowWhy()


def verse2():
    swallowed("spider", ",")
    wriggled()
    dontKnowWhy()


def verse3():
    swallowed("bird", ",")
    wriggled()
    dontKnowWhy()


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

    # horse verse
    lastverse()

    # new verse
    verse6()


# call main
main()
