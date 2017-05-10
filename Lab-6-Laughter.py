# Dan Ryan
# Lab 6: Laughter
# Plus
# This will make fun outputs to show the user!


def main():
    # Ask for user input
    name = input('Enter the name: ')
    rating = input('Enter the evilness rating: ')
    # Validate user inputs
    while name == '':
        # user input error for Name
        print('Error in input. Name cannot be blank.')
        name = input('Try again. Enter the name: ')
    while not rating.isdigit():
        # user input error for rating
        print('Error in input. Rating must be a non-negative integer.')
        rating = input('Try again. Enter the evilness rating: ')
    # Convert rating from string to int
    rating = int(rating)
    # Generate the laugh to be printed, then print it
    laugh = 'Bwa' + 'ha' * rating
    print('My name is %s. %s.' % (name, laugh))


# call main
main()
