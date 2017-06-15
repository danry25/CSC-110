# Dan Ryan
# Lab 11: Exception Handling
# Plus
# Doing some math on user inputted numbers, mostly basic counting & division.


# Main function, where all the logic is stored
def main():
    # Storage variables
    total = 0
    count = 0
    value = '0'
    # Repeatedly add to those storage variables and ask for user input!
    while(value != 'end'):
        # Ask for user input
        value = input('Enter a number (\'end\' to exit): ')
        if value.isdigit():
            # Turn the user input into an int before storing
            total += int(value)
            # Add to those storage variables
            count += 1
        # Check if value is end, skip if so
        elif value == 'end':
            pass
        # Handle Non-numeric cases that are not end
        else:
            print('Non-numeric input ignored')
    # Tell the user how many values they entered, and what the average is
    print('You entered', count, 'values')
    if not count == 0:
        print('The average value is', total/count)
    else:
        print('The average cannot be calculated.')


# Run the main function
main()
