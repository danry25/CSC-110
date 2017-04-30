# Dan Ryan
# Lab 5: ASCII Art
# Plus
# This script prints fun ASCII art and explores the use of functions!


def box():  # Printing a box
    print('+------+')
    print('|      |')
    print('|      |')
    print('|      |')
    print('+------+')


def uparrow():  # Print a component so we can reduce redundancy!
    print('   /\\')
    print('  /  \\')
    print(' /    \\')


def downarrow():  # Here's another component I refactored out!
    print(' \\    /')
    print('  \\  /')
    print('   \\/')


def diamond():  # Oooh, a diamond! Lets show the user
    uparrow()
    downarrow()


def X():  # Time to go print an X
    downarrow()
    uparrow()


def rocket():  # Lets print a rocketship!
    uparrow()
    box()
    print('|United|')
    print('|States|')
    box()
    uparrow()
    print(' ')


def main():
    box()  # Outputting a box
    print()
    diamond()  # Outputting a diamond
    print()
    X()  # Outputting an X
    print()
    rocket()  # Ooo, a rocket!


main()
