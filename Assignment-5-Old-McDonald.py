# Dan Ryan
# Assignment 5: Old McDonald
# Challenge
# This script calculates statistics on sentences that were inputted by the user.


def title():
    print("Old McDonald\n")


def verse(animal, sound):
    print("Old McDonald had a farm, E-I-E-I-O.")
    print("And on that farm he had a {}, E-I-E-I-O.".format(animal))
    print("With a {sound}-{sound} here, and a {sound}-{sound} there.".format(sound=sound))
    print("Here a {sound}, there a {sound}, everywhere a {sound}-{sound}.".format(sound=sound))
    print("Old McDonald had a farm, E-I-E-I-O.\n")


def main():
    title()
    verse('chicken', 'cluck')
    verse('cow', 'moo')
    verse('duck', 'quack')


main()
