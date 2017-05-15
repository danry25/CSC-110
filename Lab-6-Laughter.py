# Dan Ryan
# Lab 6: Laughter
# Plus
# This will make fun outputs to show the user!


def main():
    nameretry = 1
    ratingretry = True
    # Ask for user input
    name = input('Enter the name: ')
    rating = input('Enter the evilness rating: ')
    name = name.strip()
    # Validate user inputs
    while name == '' and nameretry <= 2:
        # user input error for Name
        print('Error in input. Name cannot be blank.')
        name = input('Try again. Enter the name: ')
        nameretry += 1
    else:
        if nameretry <= 2:
            pass
        else:
            print("You've tried entering a name 3 times, we're giving up & setting a default value")
            name = "Krampus"
    # while not rating.isdigit():
    #     # user input error for rating
    #     print('Error in input. Rating must be a non-negative integer.')
    #     rating = input('Try again. Enter the evilness rating: ')
    # Convert rating from string to int
    # rating = int(rating)
    # Generate the laugh to be printed, then print it
    while ratingretry:
        rating2 = int(rating)
        if rating2 == 0:
            laugh = 'Hee hee'
            ratingretry = False
        elif rating[0] == '-' and rating2 <= 7 and rating2 >= -7 and len(rating) == 2:
            laugh = 'Ho' * int(rating[1])
            ratingretry = False
        elif rating2 <= 7 and rating2 >= -7:
            laugh = 'Bwa' + 'ha' * rating2
            ratingretry = False
        else:
            rating = input('Try again. Enter the evilness rating: ')
            ratingretry = True

    print('My name is %s. %s.' % (name, laugh))


# call main
main()
