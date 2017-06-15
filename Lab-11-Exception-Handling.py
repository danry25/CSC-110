# Dan Ryan
# Lab 11: Exception Handling
# Plus
# Doing some math on user inputted numbers, mostly basic counting & division.


# Main function, where all the logic is stored
def main():
    # Storage variables
    total = 0
    count = 0
    value = ''
    # Repeatedly add to those storage variables and ask for user input!
    while(value != 'end'):
        try:
            # Ask for user input
            value = input('Enter a number (\'end\' to exit): ')
            # Turn the user input into an int before storing
            total += int(value)
            # Add to those storage variables
            count += 1
        # Handle Non-numeric cases
        except ValueError:
            # Check if value is end, complain if not end
            if not value == 'end':
                print('Non-numeric input ignored')
    # Tell the user how many values they entered, and what the average is
    print('You entered', count, 'values')
    try:
        print('The average value is', total/count)
    except ZeroDivisionError:
        print('The average cannot be calculated.')


# Run the main function
main()
