# Dan Ryan
# Lab 8: Jabber
# Plus
# Find some words containing a string or a letter in a file

# Bring in sys.argv to handle runtime options
import sys as sys

# Open, read & parse file into an array so we can work with it
all_words = []
# Open file
with open('jabber.txt') as j:
    # Process line into variable
    line = j.readline()
    # Loop through each line and process it into all_words
    while line != "":
        all_words += line.strip().split(" ")
        line = j.readline()


# Function for finding a letter or string in a word
def letterProcessor(letter):
            # All the words that have this letter in them
            letter_words = []
            # Loop through each word
            for word in all_words:
                # Append these words to the array if they match
                if letter in word.lower():
                    letter_words.append(word)
            # Output all these words into a labeled set
            out.write("{} words:\n".format(letter.upper()))
            out.write(" ".join(letter_words))
            out.write("\n")


# Write the labeled set all to a file
with open('jabber-selected-words.txt', 'w') as out:
    # Check if any arguments were passed when running the file
    try:
        letter = sys.argv[1]
        letterProcessor(letter)
    # If not, just do the whole alphabet
    except:
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            letterProcessor(letter)
