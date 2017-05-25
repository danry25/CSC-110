# Dan Ryan
# Lab 8: Jabber
# Plus
# Find some words containing a string in a file

# Bring in sys.argv to handle runtime options
import sys as sys

# Open, read & parse file into an array so we can work with it
all_words = []
letter = ''
with open('jabber.txt') as j:
    line = j.readline()
    while line != "":
        all_words += line.strip().split(" ")
        line = j.readline()


def letterProcessor():
            letter_words = []  # All the words that have this letter in them
            for word in all_words:
                if letter in word.lower():
                    letter_words.append(word)
            out.write("{} words:\n".format(letter.upper()))
            out.write(" ".join(letter_words))
            out.write("\n")


with open('jabber-selected-words.txt', 'w') as out:
    try:
        letter = sys.argv[1]
        letterProcessor()
    except:
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            letter = letter
            letterProcessor()
