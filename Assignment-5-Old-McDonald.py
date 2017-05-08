# Dan Ryan
# Assignment 5: Old McDonald
# Challenge
# This script calculates statistics on sentences that were inputted by the user.


def title():  # Prints a nice little title :P
    print("Old McDonald\n")


def helper():  # Prints the begining & ending refrain for each stanza of th song
        print("Old McDonald had a farm, E-I-E-I-O.")


def verse(animal, sound):  # Prints the core of the song, covering the animals & their sounds
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


def newVerse():  # Prompts for custom verse
    animal = input("Enter an animal: ")
    sound = input("Enter the sound the {} makes: ".format(animal))
    print()
    verse(animal, sound)


def main():  # Runs all the functions we created!
    title()
    verse('chicken', 'cluck')
    verse('cow', 'moo')
    verse('duck', 'quack')
    newVerse()  # Print first custom verse
    fifthVerse = input("Do you want to have a fifth verse (yes/no)? ")
    print()
    if fifthVerse == "no":  # Check if the user wants a 5th verse of the song
        pass
    else:
        newVerse()


main()  # Actually run said functions and make 'em work
