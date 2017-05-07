# Dan Ryan
# Assignment 5: Old McDonald
# Challenge
# This script calculates statistics on sentences that were inputted by the user.


def title():
    print("Old McDonald\n")


def helper():
        print("Old McDonald had a farm, E-I-E-I-O.")


def verse(animal, sound):
    if animal[0] in "AEIOUaeiou":
        anAnimal = "an"
    else:
        anAnimal = "a"
    if sound[0] in "AEIOUaeiou":
        anSound = "an"
    else:
        anSound = "a"
    helper()
    print("And on that farm he had {} {}, E-I-E-I-O.".format(anAnimal, animal))
    print("With {anSound} {sound}-{sound} here, and {anSound} {sound}-{sound} there.".format(sound=sound, anSound=anSound))
    print("Here {anSound} {sound}, there {anSound} {sound}, everywhere {anSound} {sound}-{sound}.".format(sound=sound, anSound=anSound))
    helper()
    print()


def newVerse():
    animal = input("Enter an animal: ")
    sound = input("Enter the sound the {} makes: ".format(animal))
    print()
    verse(animal, sound)


def main():
    title()
    verse('chicken', 'cluck')
    verse('cow', 'moo')
    verse('duck', 'quack')
    newVerse()
    fifthVerse = input("Do you want to have a fifth verse (yes/no)? ")
    print()
    if fifthVerse == "no":
        pass
    else:
        newVerse()


main()
