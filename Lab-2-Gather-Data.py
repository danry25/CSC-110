# Dan Ryan
# Lab 2: Gather Data
# Plus
# This script should print 4 lines, the first being the full name,
# the next being the initials, with the 3rd line printing your name,
# and the next printing your age, the following printing your age in dog years,
# and the final line printing your age & age in dog years next year

# Gathering user input
firstname = input("What is your first name? ").strip()
lastname = input("What is your last name? ").strip()
age = int(input("What is your age? "))
initials = firstname[0] + lastname[0]

# Returning calculations and info to user
print("It's nice to meet you, " + firstname + " " + lastname + ".")
print("Your initials are " + initials + ".")
print("This year, you're {} years old.".format(age))
print("That's {}, in \"dog years\".".format(age * 7))
print("Next year, you'll be {}, or {} in \"dog years\".".format(age + 1, (age + 1) * 7))
